int flag1 = 0;
int flag2 = 0;
int flag3 = 0;
int dimL = 99;
int Array[9];
String start = "Listo para iniciar";
String a = "He recibido tu confirmacion con exito";
void setup() {
pinMode(13, OUTPUT);
digitalWrite(13, HIGH);
Serial.begin(9600);
Serial.flush();
}

void loop() {

 if(flag1 == 0){
  for(int i = 0; i < start.length(); i++){
    Serial.write(start.charAt(i)); 
  }
  Serial.write('\n');
  flag1 = 1; 
    }

    if(Serial.available() > 0 && flag1 == 1 && flag2 == 0){
      String data = Serial.readString();
      if(data == "ok"){
        for(int i = 0; i < a.length(); i++){
          Serial.write(a.charAt(i));
          }
          Serial.write('\n');
          flag2 = 1;
        }
      }
      if(Serial.available() > 0 && flag2 == 1 && flag3 == 0){
        dimL = Serial.parseInt();
        Serial.print(dimL);
        
        if(dimL < 99){
          for (int i = 0; i < dimL + 1; i++){
            int nArr = Serial.parseInt();
            Array[i] = nArr;
            }
          Serial.print(Array[0]);
          Serial.write('\n'); // Añade un carácter de nueva línea
          flag3 = 1;
          }
        }
  }
