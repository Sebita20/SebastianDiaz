# Actividad 5: convertir numeros romanos a decimales
def romano_a_dec(rom):
    romanos = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    if len(rom) == 1:
        return romanos[rom]
    elif  romanos[rom[-2]] != None and romanos[rom[-2]] < romanos[rom[1]]:
        return romano_a_dec(rom[1]) - romanos[rom[:-1]] 
    else:
        return romanos[rom[1]] + romano_a_dec(rom[:-1])
    

print(romano_a_dec("XX"))


# Actividad 22: Mochila Jedi
def usar_la_fuerza(mochila):
    objetos = 1
    if len(mochila) == 0:
        return " La mochila está vacía, no se encotró un sable de luz."
    elif mochila[-1] == "sable de luz":
        return f"Luke, encontró su sable de luz. Tuvo que sacar: {objetos} objetos de su mochila"
    else:
        objetos += 1
        return usar_la_fuerza(mochila[:-1])

print(usar_la_fuerza(mochila=["block de hojas","goma de borrar","sable de luz","lapicera", "boligoma"]))