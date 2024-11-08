cipher = input("Ingresa tu mensaje: ")
text = ''
shift = 1  # Número de posiciones para el cifrado

for char in cipher:
    if char == ' ':
        text += ' '
        continue
    if char.isalpha():
        char = char.upper()
        code = ord(char) - shift
        if code < ord('A'): 
            code += 26
        text += chr(code)

print(text)
