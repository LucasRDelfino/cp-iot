int ledPin = 13;  // Pino do LED (pode alterar para o pino que desejar)
char receivedData;  // Variável para armazenar o dado recebido

void setup() {
  Serial.begin(9600);  // Inicia a comunicação serial com baud rate 9600
  pinMode(ledPin, OUTPUT);  // Configura o pino do LED como saída
  digitalWrite(ledPin, LOW);  // Inicialmente, o LED está apagado
}

void loop() {
  if (Serial.available() > 0) {  // Verifica se há dados na porta serial
    receivedData = Serial.read();  // Lê o dado recebido

    // Verifica o valor recebido
    if (receivedData == '1') {
      digitalWrite(ledPin, HIGH);  // Acende o LED (queda detectada)
    } else if (receivedData == '0') {
      digitalWrite(ledPin, LOW);  // Apaga o LED (sem queda)
    }
  }
}