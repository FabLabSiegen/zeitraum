#include <Wire.h>
#include <SPI.h>
#include <Adafruit_CAP1188.h>
#include <Time.h>
#include <Keyboard.h>

int NUM_ADUINO = 1;
int LAST_SENSOR_PREV = 13;
int LAST_SENSOR = 13;


void setup() {
    Serial.begin(9600);

    Keyboard.begin();
}

void sendKeyboardAction(int i) {
    int valuetopost=(NUM_ADUINO * (LAST_SENSOR_PREV+1)) + LAST_SENSOR-i;//reading from highest to lowest
    Serial.print("Sending "); Serial.println(valuetopost);
    if(valuetopost>9){
      valuetopost+=97-9;//changing higher numbers to chars starting from a up to z to have a more "buttonpress" style input
      char chartopost=valuetopost;
      Keyboard.write(chartopost);
    }
    else{
      Keyboard.write(valuetopost);
    }
    //Keyboard.write(KEY_RETURN);
}

int touchedPort = -1;
bool touched = false;
time_t touchTime = time_t(0.5);
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
            // Touch lasted 2 secs
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
    for (int i = 0; i < LAST_SENSOR + 1; i++) {
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
