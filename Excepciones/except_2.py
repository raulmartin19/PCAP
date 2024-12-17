
try:
    y=1/0
except (ZeroDivisionError,ArithmeticError):
    print("Hubo un problema en la operacion")
except:
    print("Algo falla aqui...")
    
print("FIN")


