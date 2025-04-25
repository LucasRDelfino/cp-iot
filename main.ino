int buzzerPin = 8;

void setup() {
  Serial.begin(9600);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char receivedData = Serial.read();

    if (receivedData == '1') {
      tone(buzzerPin, 1000); // 1000 Hz = som agudo
    } else if (receivedData == '0') {
      noTone(buzzerPin);     // Desliga o som
    }
  }
}