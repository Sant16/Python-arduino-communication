import serial
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM7'
ser.open()
while True:
    mensaje = input('Ingrese mensaje que va a enviar al arduino: \n')
    ser.write(mensaje.encode())
