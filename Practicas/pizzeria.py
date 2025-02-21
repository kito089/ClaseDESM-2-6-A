while True:
    print("Seleccione: ")
    print("\t1) Pizza")
    print("\t2) Hamburguesa")
    print("\t3) Ensalada")
    print("\t0) Salir")
    try:
        ing = int(input("Opción: "))
        match ing:
            case 1:
                print("Pizza ... $10")
            case 2:
                print("Hamburguesa ... $8")
            case 3:
                print("Ensalada ... $6")
            case 0:
                print("Saliendo del programa")
                break
            case _:
                print("Opción inválida (solo numeros del 0 al 3)")
    except:
        print("La opcion debe de ser un numero, favor de volver a seleccionar")
        continue
