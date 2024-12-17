def read_int(prompt, min, max):
    while True:
        try:
              value = int(input(prompt))
              if min <= value <= max:
                return value
              else:
                  raise ValueError
              
        except ValueError:
            print("Numero incorrecto")


v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)
    
