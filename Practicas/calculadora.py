def suma(n1,n2):
    return n1+n2
def resta(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

def operaciones(op):
    try:
        n1 = float(input("Ingrese el primer numero: "))
        n2 = float(input("Ingrese el segundo numero: "))
        match op:
            case 1:
                print(n1," + ",n2," = ", suma(n1,n2))
            case 2:
                print(n1," - ",n2," = ", resta(n1,n2))
            case 3:
                print(n1," * ",n2," = ", mult(n1,n2))
            case 4:
                if n2 != 0:
                    print(n1," / ",n2," = ", div(n1,n2))
                else:
                    print("No se puede dividir entre 0")
        menu()
    except:
        print("Solo se pueden usar numeros, no caracteres especiales")
        operaciones(op)

def menu():
    print("Elija una de las siguientes opciones: ")
    print("\t1) Suma")
    print("\t2) Resta")
    print("\t3) Multiplicacion")
    print("\t4) Division")
    print("\t0)Salir")
    try:
        op = int(input())
        if op > 0 and op < 5:
            operaciones(op)
        elif op == 0:
            print("Adios uwu")
        else:
            int("uwu")
    except:
        print("La opcion seleccionada debe der ser un numero entre 0-4")
        menu()

menu()