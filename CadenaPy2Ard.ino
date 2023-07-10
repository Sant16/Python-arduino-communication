void setup() {
  Serial.begin(9600); // Iniciar la comunicación serial
  pinMode(13, OUTPUT); // Configurar el pin 9 como salida
  digitalWrite(13, HIGH);
}

void loop() {
  if (Serial.available() > 0) { // Verificar si hay datos disponibles en el puerto serial
    String cadena = Serial.readString(); // Leer la cadena de texto recibida del puerto serial
    if (cadena == "on led") { // Si el mensaje recibido es "encender_led"
      digitalWrite(13, HIGH); // Encender el LED
 
    }
     if (cadena == "off led") { // Si el mensaje recibido es "encender_led"
      digitalWrite(13, LOW); // Encender el LED
    }
  }
}
