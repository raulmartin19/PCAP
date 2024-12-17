def mal_asunto(n):
    try:
        return n/0
    except:
        print("Lo hice otra vez")
        raise 

try:
    mal_asunto(0)
except ArithmeticError:
    print("QUE PASOO")
    exit(0)
    
print("FIN")