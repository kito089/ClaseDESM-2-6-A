import random
import math
import numpy as np
import matplotlib.pyplot as plt

num='''7
15
15
20
17
19
10
5
3
3
4
8
11
13
10
6
2
9
8
15
2
13
12
4
1'''

TRA = 25

def intervalo():
    return round(1+3.322*math.log(TRA,10))
def amplitude():
    return (comple[-1]-comple[0])/intervalo()

lista = num.split("\n")
print(lista)
dat = []
for i in lista:
    # d = i.split("\t")
    # for j in d:
        dat.append(float(i))

comple = sorted(dat)
print("Datos ordenados: ", comple)
print("Rango: ", comple[-1]-comple[0])
print("Intervalo: ", 1+3.322*math.log(TRA,10), " redondeado a: ", intervalo())
print("Amplitud: ", amplitude())
print("Tabla de distribucion de frecuencias: ")

tabla = []
sumas = comple[0]
acu = 0

for i in range(intervalo()):
    tabla.append([i+1])
    sumas += amplitude()
    fre = 0
    for j in comple:
        #print("if ", j, ">=", sumas - amplitude(), " and ", j, "<", sumas)
        if j >= sumas - amplitude() and j <= sumas:
            fre += 1
    acu += fre
    marca = round((sumas - amplitude() + sumas)/2,2)
    tabla[-1].append(str(round(sumas-amplitude(),2))+" - "+str(round(sumas,2)))
    tabla[-1].append(fre)
    tabla[-1].append(acu)
    tabla[-1].append(marca)
print(np.array(tabla))

matriz = np.array(tabla)

# Extraer datos relevantes
intervalos = matriz[:, 1]  # Intervalos de clase
frecuencias = matriz[:, 2].astype(int)  # Frecuencias
frecuencia_acumulada = matriz[:, 3].astype(int)  # Frecuencia acumulada

# Crear la figura
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Generar el histograma de frecuencia con intervalos de clase en el eje X
axes[0, 0].bar(intervalos, frecuencias, width=1.0, color='skyblue', edgecolor='black', align='center')
axes[0, 0].set_title('Histograma de Frecuencia')
axes[0, 0].set_xlabel('Intervalo de Clase')
axes[0, 0].set_ylabel('Frecuencia')
axes[0, 0].set_xticklabels(intervalos, rotation=45, ha='right')  # Rotar etiquetas para mejor legibilidad

# Generar el polígono de frecuencia
marcas_de_clase = matriz[:, 4].astype(float)  # Marcas de clase
axes[0, 1].plot(marcas_de_clase, frecuencias, marker='o', linestyle='-', color='orange')
axes[0, 1].set_title('Polígono de Frecuencia')
axes[0, 1].set_xlabel('Marca de Clase')
axes[0, 1].set_ylabel('Frecuencia')
axes[0, 1].grid(True)

# Generar el polígono de frecuencia acumulada
axes[1, 0].plot(marcas_de_clase, frecuencia_acumulada, marker='o', linestyle='-', color='purple')
axes[1, 0].set_title('Polígono de Frecuencia Acumulada')
axes[1, 0].set_xlabel('Marca de Clase')
axes[1, 0].set_ylabel('Frecuencia Acumulada')
axes[1, 0].grid(True)

# Mostrar la tabla de distribución de frecuencias
axes[1, 1].axis('off')  # Ocultar el eje
column_labels = ['Intervalo', 'Frecuencia', 'Frecuencia Acumulada', 'Marca de Clase']
table_data = matriz[:, 1:]  # Excluir la columna del número de intervalo
table = axes[1, 1].table(cellText=table_data, colLabels=column_labels, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Ajustar el diseño
plt.tight_layout()
plt.show()