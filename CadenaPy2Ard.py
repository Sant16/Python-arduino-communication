import serial
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM7'
ser.open()
while True:
    ser.write(b'A')
    time.sleep(3)
    ser.write(b'a')
    time.sleep(3)
