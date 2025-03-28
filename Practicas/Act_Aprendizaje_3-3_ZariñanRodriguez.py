def encontrar_cambio(cambio, monedas):
    if cambio == 0:
        return []  # Si no queda cambio se termina la recursion
    
    validas = [m for m in monedas if m <= cambio] ## Agregar a una lista las monedas menores al cambio
    if not validas:
        if cambio > 0: ## Si no hay monedas menores al cambio y el cambio es mayor a 0 no se puede hacer el cambio
            return ["Se dio todo el cambio, falta: "+str(cambio)]
        return []     
    
    mejor = max(validas) ## Entre las monedas validas se elige la mayor
    monedas.pop(monedas.index(mejor)) ## Se elimina la moneda mayor de la lista de monedas
    return [mejor] + encontrar_cambio(cambio - mejor, monedas) ## Se repite la funcion para encontrar todas las monedas mayores

# Ejemplo de teams
cambio = 27
monedas = [1, 2, 5, 10, 20]
resultado = encontrar_cambio(cambio, monedas)

print("Cambio total:", cambio)
print("Monedas utilizadas:", resultado)

# Ejemplo de propio
cambio = 50
monedas = [10, 1, 5, 2, 5, 10, 20]
resultado = encontrar_cambio(cambio, monedas)

print("Cambio total:", cambio)
print("Monedas utilizadas:", resultado)

# Ejemplo de error
cambio = 40
monedas = [1, 2, 5, 10, 20]
resultado = encontrar_cambio(cambio, monedas)

print("Cambio total:", cambio)
print("Monedas utilizadas:", resultado)