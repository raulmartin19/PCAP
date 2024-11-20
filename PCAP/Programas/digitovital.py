while True:
    fecha = input("Introduce tu fecha de nacimiento (en formato AAAAMMDD): ")
    if fecha.isnumeric() and len(fecha) == 8:
        break
    print("Debes introducir una fecha válida en el formato AAAAMMDD.")

suma = sum(int(c) for c in fecha)
while suma >= 10:
    suma = sum(int(c) for c in str(suma))

print("Tu digito vital es:", suma)
