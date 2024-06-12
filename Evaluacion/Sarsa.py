def bernstain (cadena):
    h = 0 
    for caracter in cadena: 
        h = h * 33 + ord(caracter)
    return h 

print(bernstain('hole') % 13)