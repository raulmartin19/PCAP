while True:
    fecha = input("Introduce tu fecha de nacimiento (en formato AAAAMMDD): ")
    if fecha.isnumeric() and len(fecha) == 8:
        break
    print("Debes introducir una fecha válida en el formato AAAAMMDD.")
    
digito=0
suma=0

for c in fecha:
    suma += int(c)

if suma < 10:
    digito=suma
else:
    for c in str(suma):
        digito+= int(c)

print("Tu digito vital es:", suma)