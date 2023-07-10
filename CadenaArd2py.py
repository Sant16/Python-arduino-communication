import serial

# Configurar puerto serial
ser = serial.Serial('COM7', 9600)

# Leer una cadena de texto desde Arduino
message = ''
while True:
    incoming = ser.read().decode()
    if incoming == '\n':
        break
    message += incoming

print(message)
