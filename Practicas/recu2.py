def suma_numeros(n): #Definicion de la funcion
    if n < 0: #Evaluar si un numero es menor
        return "Se debe de utilizar un numero positivo" #Retornar mensaje de error
    elif n == 0: #Evaluar fin de la funcion
        return 0 #Terminar la funcion
    return n + suma_numeros(n-1) #Aplicacion de recursividad

print(suma_numeros(5)) #Imprimir caso valido
print(suma_numeros(-5)) #Imprimir caso no valido