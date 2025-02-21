est = []
def promedio(lista):
    x = 0
    for i in lista:
        x = x + i
    return x/len(lista)

def pedir():
    global est
    try:
        ps = float(input("Escribe la estatura de la persona "+str(len(est)+1)+" : (solo digitos) "))
        est.append(ps)
    except:
        print("Solo se admiten numeros")
        pedir()

def main():
    global est
    while True:
        pedir()
        try:
            op = int(input("Desea continuar? 1=Si, Cualquier otra tecla = No "))
            if op != 1:
                break
        except:
            break

    print("El promedio es: ", promedio(est))

main()