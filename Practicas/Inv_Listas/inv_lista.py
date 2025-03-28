import csv
import os

# Archivo para almacenar el inventario
ARCHIVO_INVENTARIO = "inventario.csv"

def cargar_productos():
    """Carga los productos desde el archivo CSV y los devuelve como una lista de diccionarios"""
    productos = []
    if os.path.exists(ARCHIVO_INVENTARIO):
        try:
            with open(ARCHIVO_INVENTARIO, 'r', newline='', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    try:
                        fila['id'] = int(fila['id'])
                        fila['precio'] = float(fila['precio'])
                        fila['stock'] = int(fila['stock'])
                        productos.append(fila)
                    except (ValueError, KeyError):
                        print(f"Error en formato de datos en fila: {fila}")
            print(f"Se cargaron {len(productos)} productos del inventario.")
        except Exception as e:
            print(f"Error al cargar el inventario: {str(e)}")
    else:
        print("No se encontró archivo de inventario. Se creará uno nuevo al guardar productos.")
    return productos

def guardar_productos(productos):
    """Guarda la lista de productos en el archivo CSV"""
    try:
        with open(ARCHIVO_INVENTARIO, 'w', newline='', encoding='utf-8') as archivo:
            campos = ['id', 'nombre', 'descripcion', 'precio', 'stock']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for producto in productos:
                escritor.writerow(producto)
        print(f"Inventario guardado exitosamente en {ARCHIVO_INVENTARIO}")
        return True
    except Exception as e:
        print(f"Error al guardar el inventario: {str(e)}")
        return False

def validar_entrada(mensaje, tipo):
    """Valida la entrada del usuario según el tipo especificado"""
    while True:
        try:
            valor = tipo(input(mensaje))
            if isinstance(valor, (int, float)) and valor < 0:
                print("El valor debe ser mayor o igual a cero.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

def agregar_producto(productos):
    """Solicita datos de un nuevo producto y lo agrega al inventario"""
    print("\n=== AGREGAR NUEVO PRODUCTO ===")
    nuevo_id = max([p['id'] for p in productos], default=0) + 1
    nombre = input("Nombre del producto: ").strip()
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre del producto: ").strip()
    descripcion = input("Descripción: ")
    precio = validar_entrada("Precio: $", float)
    stock = validar_entrada("Cantidad en stock: ", int)
    productos.append({'id': nuevo_id, 'nombre': nombre, 'descripcion': descripcion, 'precio': precio, 'stock': stock})
    if guardar_productos(productos):
        print(f"\nProducto '{nombre}' agregado con ID {nuevo_id}")

def buscar_producto(productos):
    """Busca productos por nombre o parte del nombre"""
    if not productos:
        print("No hay productos en el inventario.")
        return
    termino = input("Ingrese el nombre o parte del nombre a buscar: ").lower()
    encontrados = [p for p in productos if termino in p['nombre'].lower()]
    print(f"\nSe encontraron {len(encontrados)} productos:") if encontrados else print("No se encontraron productos.")

def actualizar_stock(productos):
    """Actualiza la cantidad en stock de un producto por su ID"""
    if not productos:
        print("No hay productos en el inventario.")
        return
    id_producto = validar_entrada("Ingrese el ID del producto: ", int)
    producto = next((p for p in productos if p['id'] == id_producto), None)
    if producto:
        print(f"Producto: {producto['nombre']} | Stock actual: {producto['stock']}")
        producto['stock'] = validar_entrada("Nuevo stock: ", int)
        if guardar_productos(productos):
            print(f"Stock actualizado exitosamente para '{producto['nombre']}'")
    else:
        print("Producto no encontrado.")

def eliminar_producto(productos):
    """Elimina un producto del inventario por su ID"""
    if not productos:
        print("No hay productos en el inventario.")
        return
    id_producto = validar_entrada("Ingrese el ID del producto a eliminar: ", int)
    producto = next((p for p in productos if p['id'] == id_producto), None)
    if producto:
        if input(f"¿Está seguro de eliminar '{producto['nombre']}'? (s/n): ").lower() == 's':
            productos.remove(producto)
            if guardar_productos(productos):
                print(f"Producto '{producto['nombre']}' eliminado exitosamente")
    else:
        print("Producto no encontrado.")

def menu_principal():
    """Función principal que muestra el menú y gestiona la interacción del usuario"""
    productos = cargar_productos()
    opciones = {
        1: agregar_producto,
        2: buscar_producto,
        3: actualizar_stock,
        4: eliminar_producto
    }
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
        print("1. Agregar producto\n2. Buscar producto\n3. Actualizar stock\n4. Eliminar producto\n5. Salir")
        opcion = validar_entrada("Seleccione una opción (1-5): ", int)
        if opcion == 5:
            print("¡Gracias por usar el sistema!")
            break
        elif opcion in opciones:
            opciones[opcion](productos)
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()
