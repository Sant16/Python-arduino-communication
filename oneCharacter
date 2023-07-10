import serial

# Configurar puerto serial
ser = serial.Serial('COM7', 9600)

while True:
 # Leer la respuesta de Arduino
 response = ser.read()
 response_deco = response.decode('ascii')
 print(response_deco)
