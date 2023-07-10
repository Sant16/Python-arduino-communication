void setup() {
  Serial.begin(9600); // Iniciar la comunicación serial
  pinMode(13, OUTPUT); // Configurar el pin 9 como salida
}

void loop() {
  if (Serial.available() > 0) { // Verificar si hay datos disponibles en el puerto serial
    char c = Serial.read(); // Leer el dato disponible del puerto serial
    if (c == 'A') { // Verificar si el dato recibido es la letra 'A'
      digitalWrite(13, HIGH); 
    }
        if (c == 'a') { // Verificar si el dato recibido es la letra 'A'
      digitalWrite(13, LOW);  
    }
  }
}
