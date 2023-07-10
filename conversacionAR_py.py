import serial
import time

flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
lista = [1, 2, 311, 4, 5]
start = ''
conf = 'ok'
conf2 = ''
arduino = serial.Serial('COM7', 9600)

while flag1 == 0:
    incoming = arduino.read().decode()
    start += incoming
    if incoming == '\n':
        flag1 = 1
print(start)
while flag2 == 0 and flag1 == 1:
    arduino.write(conf.encode())
    incoming = arduino.read().decode()
    conf2 += incoming
    if incoming == '\n':
        flag2 = 1
print(conf2)

while flag3 == 0 and flag2 == 1:
    dimL = len(lista)
    arduino.write(str(dimL).encode())
    dimLr = arduino.read().decode()
    print('La dimension del arreglo es: ',dimLr)
    flag3 = 1

while flag4 == 0 and flag3 == 1:
    for i in lista:
        arduino.write(str(i).encode())
        time.sleep(1)
    arduino.flushInput()
    nc = arduino.readline().decode().strip()
    n = int(nc)
    print(n)
    flag4 = 1
