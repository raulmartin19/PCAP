'''
El orden de las excepciones siempre va desde la mas concreta a la mas general
'''

try:
    y=1/0
except ZeroDivisionError:
    print("Divsion entre 0")
except ArithmeticError:
    print("Problema aritmetico")
except:
    print("Algo falla aqui...")
    
print("FIN")


