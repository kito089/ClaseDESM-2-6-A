p = float(input("Dame el p: "))
n = float(input("Dame el numero de datos: "))
z = float(input("Dame el Z: "))

def uwu():
    return z*(((p*(1-p))/(n))**0.5)

print("Primer resultado: ", p+uwu())
print("Segundo resultado: ", p-uwu())