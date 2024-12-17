import math

x = float(input("Ingresa un número: "))
try:
    assert x >= 0.0
except AssertionError:
    print("El numero debe ser mayor que 0")
    exit(1)

x = math.sqrt(x)

print(x)