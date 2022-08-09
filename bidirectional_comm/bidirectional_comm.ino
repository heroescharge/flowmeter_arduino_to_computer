#define BAUD 115200
#define AIN A0

float voltageReading;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(BAUD);

  pinMode(AIN, INPUT);

  getReading();
}

void loop() {
  
  if (Serial.available() > 0) {
     getReading();
     Serial.end();
     Serial.begin(BAUD);     
  }
  
}

void getReading() {
  voltageReading = analogRead(AIN);
  Serial.println(voltageReading);
}
