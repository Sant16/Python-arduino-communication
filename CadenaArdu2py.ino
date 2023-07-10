void setup() {
  Serial.begin(9600);
}

void loop() {
  String message = "Hola python! estoy listo para comunicarme contigo";
  for (int i = 0; i < message.length(); i++) {  //length fuction give you the numbers of index of your message
    Serial.write(message.charAt(i));
    delay(10);
  }
  Serial.write('\n');
  delay(1000);
}
