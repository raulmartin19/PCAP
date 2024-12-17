from imprime_pares import imprime_pares as impp

line=input('ingresa una linea de numero, separalos con espacio')
strings=line.split()
total=0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:",total)
except:
    print("Error: '"+substr+"' no es un numero.")

impp(strings)