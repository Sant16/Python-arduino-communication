import serial
import numpy as np
import matplotlib.pyplot as plt

flag = 0

# Función para actualizar la gráfica en tiempo real
def update_plot():
    ax.clear()
    ax.axis([0, 200, -2, 2])
    ax.plot(datos_seno, label='Seno', linestyle='-', color='r', linewidth=3)
    ax.plot(datos_coseno, label='Coseno', linestyle='none', marker='.', markersize=3, color='b', linewidth=0.1)
    ax.legend(loc='upper left')  # Fijar la posición de la leyenda en la esquina superior izquierda
    plt.draw()

# Configuración de la comunicación serial
ser = serial.Serial('COM7', 9600, timeout=1)

# Lista para almacenar los datos de la señal
datos_seno = []
datos_coseno = []

# Configuración de la gráfica
plt.ion()  # Modo interactivo para graficar en tiempo real
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) #parcelas, depende si se quiere dividir la pantalla para varias

while True:
    # Leer un valor del puerto serial
    dato = ser.readline().decode('ascii').strip()
    if flag == 1:
        datos = dato.split('|')
        if len(datos) == 2:
            try:
                seno = float(datos[0])
                coseno = float(datos[1])

                datos_seno.append(seno)
                datos_coseno.append(coseno)
                if len(datos_coseno) > 200 and len(datos_seno) > 200:
                    datos_seno = []
                    datos_coseno = []

                update_plot()

            except ValueError:
                print("Error: No se pudieron convertir los datos a números.")
        else:
            print("Error: Datos incompletos.")
            flag = 0
    flag = 1

    plt.pause(0.001)  # Pausar para permitir la actualización de la gráfica
