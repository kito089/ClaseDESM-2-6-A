total_inventario = 0  

while True:
    print("Ingrese:")
    nombre = input("    Nombre del producto: ")
    
    while True:
        precio = float(input("    Precio del producto: "))
        if precio <= 0:
            print("El precio debe de ser mayor a 0")
        else:
            break
    
    cantidad = int(input("    Cantidad del producto: "))
    
    print("Resumen del producto:")
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio}")
    print(f"Cantidad: {cantidad}")
    
    total_prod = cantidad * precio
    
    if total_prod >= 50:
        total_prod *= 0.9  
        print("Se aplicó un 10% de descuento por superar un monto de 50")
    
    print(f"Valor total: {total_prod}")
    
    if cantidad > 20:
        print("Estado: Stock suficiente")
    elif cantidad > 0:
        print("Estado: Bajo stock")
    else:
        print("Estado: Agotado")
    
    total_inventario += total_prod
    
    op = int(input("¿Desea agregar otro producto? (0 para terminar, cualquier otro número para continuar): "))
    if op == 0:
        break

print(f"Valor total del inventario combinado: {total_inventario}")

