import pandas as pd

nom = int(input("Ingrese el numero de datos: "))

datos = []
frec = []
x = 0
x2 = 0
x3 = 0
total = 0 

for i in range(nom):
    datos.append(float(input("ingrese el dato {}: ".format(i+1))))
    frec.append(int(input("ingrese su frecuencia: ")))

    x += datos[i]*frec[i]
    total += frec[i]

prom = float(x/total)
medi = sorted(datos)
if len(medi) % 2 == 0:
    mediana = (medi[len(medi)//2] + medi[len(medi)//2-1])/2
else:
    mediana = medi[len(medi)//2]

frec_list = pd.Series(datos)          # Creas la lista, con los datos que sean necesarios 

frecuencias = frec_list.value_counts()
moda = []
if frecuencias.iloc[0] == frecuencias.iloc[1]:
    moda.append(frecuencias.index[0])
    moda.append(frecuencias.index[1])
else:
    moda.append(frecuencias.index[0])

for i in range(nom):
    if (datos[i]-prom)>=0:
        x2 += float((datos[i]-prom)*frec[i])
    else:
        x2 += float((prom-datos[i])*frec[i])
    x3 += float(((datos[i]-prom)**2)*frec[i])


print("La media es: {}".format(prom))
print("La moda es: {}".format(moda))
print("La mediana es: {}".format(mediana))
print("La desviacion media es: {}".format(x2/total))
print("La varianza es: {}".format(x3/total))
print("La desviacion tipica/estandar es: {}".format((x3/total)**0.5))