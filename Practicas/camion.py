def viaje(gan):
    dest = input("Ingrese el destino del viaje: ")
    dist = float(input("Ingrese la distancia en kilómetros: "))
    tar = float(input("Ingrese la tarifa por kilómetro: "))
    costo = dist * tar
    gan += costo
    print(f"Viaje a {dest} registrado. Costo del viaje: ${costo:.2f}. Ganancias totales {gan:.2f}")
    return gan

def combustible(gas):
    litros = float(input("Ingrese la cantidad de litros: "))
    litro = float(input("Ingrese el precio por litro: "))
    costo = litros * litro
    gas += costo
    print(f"Combustible registrado. Costo del combustible: ${costo:.2f}. Gastos totales {gas:.2f}")
    return gas

def fin(gan, gas):
    sal = gan - gas
    print(f"Ganancias: ${gan:.2f}")
    print(f"Gastos: ${gas:.2f}")
    print(f"Saldo final: ${sal:.2f}")

def main():
    gan = 0
    gas = 0
    while True:
        print("1) Iniciar un viaje")
        print("2) Registrar combustible")
        print("3) Finalizar jornada")
        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            gan = viaje(gan)
        elif opcion == '2':
            gas = combustible(gas)
        elif opcion == '3':
            fin(gan, gas)
            break
        else:
            print("Solo se admiten numeros del 1-3")

main()