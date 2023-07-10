void setup() {
  Serial.begin(9600);
}

void loop() {
  String message = "Hola Python, estoy listo";
  Serial.println(message);
  delay(1000);
}
