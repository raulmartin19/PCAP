palabra = input("Introduce la palabra a buscar: ").upper()
grupo = input("Introduce un grupo de caracteres: ").upper()

contiene = True
inicio = 0

for c in palabra:
    posicion = grupo.find(c, inicio)
    if posicion < 0:
        contiene = False
        break
    inicio = posicion + 1  

if contiene:
    print("La palabra está contenida en el grupo.")
else:
    print("La palabra no está contenida en el grupo.")
