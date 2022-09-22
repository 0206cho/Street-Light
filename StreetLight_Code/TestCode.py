#include <SoftwareSerial.h>
int bled = 10;
int led = 3;

String Serial_Data = "";

void setup(){
    pinMode(bled, OUTPUT);  // 10번 핀 출력으로 설정
    pinMode(Led, OUTPUT);   // 3번 핀 출력으로 설정

    Serial.begin(9600);

    // LED OFF
    digitalWrite(bled, LOW);
    digitalWrite(Led, LOW);

    Serial.println("해당 키를 입력해주세요");
    Serial.println();
}


void loop(){
    // 시리얼 통신으로 문자를 입력하기 위한 준비
    if(Serial.available() > 0) //시리얼 입력이 있다면
    {
        Serial_Data = (char)Serial.read();  // 한번에 한문자를 읽어 Serial_Data에 저장
        Serial.print("Serial_Data : ");
        Serial.println(Serial_Data);

        if (Serial_Data == "M") // 입력 데이터가 M(메인전구)라면
        {
            digitalWrite(bled, HIGH);
            digitalWrite(LED, LOW);
        }

        else if (Serial_Data == "S") // 입력 데이터가 S(보조전구)라면
        {
            digitalWrite(bled, LOW);
            digitalWrite(LED, HIGH);
        }
        
}
