#include <Wire.h>
#include <SPI.h>
#include <Adafruit_CAP1188.h>
#include <Time.h>
#include <Keyboard.h>

int NUM_ARDUINO = 2;//number of Arduinos before this
int LAST_SENSOR_PREV = 13;//numbers from 1 to 13 showing how many pins were connected to the leonardo
int LAST_SENSOR =1;//numbers from 0 to 12, last pin that something is connected to.
//ATTENTION: Pin 13 is not usable easily as an input, an LED is connected to it, therefore it will not be used


void setup() {
    Serial.begin(9600);

    Keyboard.begin();
}

void sendKeyboardAction(int i) {
    Keyboard.print((NUM_ARDUINO * 13) + (12-i)); //there should not be a last_sensor_prev here, if different amount of pins are used on different arduinos this goes to sh*ts
    Keyboard.write(KEY_RETURN);
}

int touchedPort = -1;
bool touched = false;
time_t touchTime = time_t(0.25);
time_t touchTimestamp = 0.0f;
void touchAction(int i) {
    if (!touched) {
        // new Touch
        touched = true;
        touchedPort = i;
        touchTimestamp = now();
        Serial.print("New touch on "); Serial.println(i);
    } else if (touchedPort == i) {
        if  (now() - touchTimestamp >= touchTime) {
            // Touch lasted touchTime secs
            touched = false;
            Serial.print("Touch completed on "); Serial.println(i);
            sendKeyboardAction(i);
        }
    } else {
        // Another Port is touched
        Serial.print("Touch interrupted with "); Serial.println(i);
        touched = false;
    }
}

void loop() {
    bool something_touched = false;
    for (int i = 12-LAST_SENSOR; i < 13; i++) {//turning arduino arround
        if (digitalRead(i) == 1) {
            touchAction(i);
            something_touched = true;
        }
    }
    if (!something_touched) {
        touched = false;
    }

    delay(100);
}
