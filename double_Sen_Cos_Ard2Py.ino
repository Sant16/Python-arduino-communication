void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}

void loop() {
  static float x = 0.0;
  float y_sen = sin(x);
  float y_cos = cos(x);

  Serial.print(y_sen);
  Serial.print("|");
  Serial.print(y_cos);
  Serial.print("\n");
  x += 0.1;
  delay(10);

  if (Serial.available() > 0) {

    String data = Serial.readString();
    if (data == "ok") {
      digitalWrite(13, HIGH);
    }
    if (data == "off") {
      digitalWrite(13, LOW);
    }
  }
}
