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
n = int(message)   #only thing you have to do its use int() function to change str to int or float respectly 
n =  n * 2
print(n)
