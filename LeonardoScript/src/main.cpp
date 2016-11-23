#include <Wire.h>
#include <SPI.h>
#include <Adafruit_CAP1188.h>
#include <Time.h>
#include <Keyboard.h>

// Reset Pin is used for I2C
#define CAP1188_RESET  9

// For I2C, connect SDA to your Arduino's SDA pin, SCL to SCL pin
// On Leonardo/Micro, SDA == Digital 2, SCL == Digital 3
#define CAP1188_SDA = 2
#define CAP1188_SCL = 3

Adafruit_CAP1188 cap28 = Adafruit_CAP1188(CAP1188_RESET);
Adafruit_CAP1188 cap29 = Adafruit_CAP1188(CAP1188_RESET);

void setup() {
    Serial.begin(9600);
    Serial.println("Testing for capacitive sensors.");

    if (!cap28.begin(0x28)) {
        Serial.println("CAP 0x28 not found");
        while (1);
    }
    Serial.println("CAP1188 0x28 found!");

    if (!cap29.begin(0x29)) {
        Serial.println("CAP 0x29 not found");
        while (1);
    }
    Serial.println("CAP1188 0x29 found!");

    Keyboard.begin();
}

void sendKeyboardAction(int i) {
    Keyboard.print(i);
    Keyboard.write(KEY_RETURN);
}

int touchedPort = -1;
bool touched = false;
time_t touchTime = time_t(2);
time_t touchTimestamp = 0.0f;
void touchAction(int i) {
    if (!touched) {
        // new Touch
        touched = true;
        touchedPort = i;
        touchTimestamp = now();
    } else {
        if (now() - touchTimestamp >= touchTime) {
            // Touch lasted 2 secs
            touched = false;
            Serial.print("Touched Port "); Serial.println(i);
            sendKeyboardAction(i);
            touchedPort = -1;
        }
    }
}

void loop() {
    uint8_t touched28 = cap28.touched();
    uint8_t touched29 = cap29.touched();

    if (touched28 == 0 && touched29 == 0) {
        // Nothing touched; reset
        touched = false;
        touchedPort = -1;
        return;
    }

    for (uint8_t i=0; i<8; i++) {
        if (touched28 & (1 << i)) {
            // First cap1188 touched
            touchAction(i);
        }
        else if (touched29 & (1 << i)) {
            // Second cap1188 touched
            touchAction(i+8);
        }
    }
    delay(50);
}
