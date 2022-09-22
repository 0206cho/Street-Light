#include <SoftwareSerial.h>
const int rxPin = 7;
const int txPin = 6;
SoftwareSerial mySerial(rxPin, txPin);
SoftwareSerial BTserial(7, 6);
int value;
float amp;

int bled = 10;
int led = 3;

void setup(){
    pinMode(A0, INPUT);
    pinMode(bled, OUTPUT);
    pinMode(led, OUTPUT);

    Serial.begin(9600);
    BTserial.begin(9600);
}

void loop(){
    value = analogRead(A0);
    amp = (((value-511)*5/1024)/0.185)*1000;
    // 1. 전압의 변화량 계산 후 측정된 값을 전압값으로 변환
    // 2. 5A용은 185mV/A의 민감도를 가짐으로 측정된 전압값에 0.185를 나누어줌
    // 3. 'mA' 단위로 바꿔줌
    Serial.print(amp);
    Serial.println("mA");
    BTserail.println(amp);

    if(amp == 0 || amp < 30){       // 메인 전구 꺼지거나 10mA 미만일 때
        digitalWrite(bled, LOW);
        digitalWrite(led, HIGH);    // 보조 전구 작동
    }
}
