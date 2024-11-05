
from Funciones2 import BinaryTree

pokemons = {
    1: {"nombre": "Bulbasaur", "tipos": ["Planta", "Veneno"]},
    2: {"nombre": "Ivysaur", "tipos": ["Planta", "Veneno"]},
    3: {"nombre": "Venusaur", "tipos": ["Planta", "Veneno"]},
    745: {"nombre": "Lycanroc", "tipos": ["Roca"]},
    5: {"nombre": "Charmeleon", "tipos": ["Fuego"]},
    6: {"nombre": "Charizard", "tipos": ["Fuego", "Volador"]},
    7: {"nombre": "Squirtle", "tipos": ["Agua"]},
    8: {"nombre": "Wartortle", "tipos": ["Agua"]},
    9: {"nombre": "Blastoise", "tipos": ["Agua"]},
    697: {"nombre": "Tyrantrum", "tipos": ["Roca", "Dragon"]},
    11: {"nombre": "Metapod", "tipos": ["Bicho"]},
    12: {"nombre": "Butterfree", "tipos": ["Bicho", "Volador"]},
    13: {"nombre": "Weedle", "tipos": ["Bicho", "Veneno"]},
    14: {"nombre": "Kakuna", "tipos": ["Bicho", "Veneno"]},
    135: {"nombre": "Jolteon", "tipos": ["Eléctrico"]},
    16: {"nombre": "Pidgey", "tipos": ["Normal", "Volador"]},
    17: {"nombre": "Pidgeotto", "tipos": ["Normal", "Volador"]},
    18: {"nombre": "Pidgeot", "tipos": ["Normal", "Volador"]},
    152: {"nombre": "Chikorita", "tipos": ["Planta"]},
    153: {"nombre": "Bayleef", "tipos": ["Planta"]},
    154: {"nombre": "Meganium", "tipos": ["Planta"]},
    155: {"nombre": "Cyndaquil", "tipos": ["Fuego"]},
    156: {"nombre": "Quilava", "tipos": ["Fuego"]},
    157: {"nombre": "Typhlosion", "tipos": ["Fuego"]},
    252: {"nombre": "Treecko", "tipos": ["Planta"]},
    253: {"nombre": "Grovyle", "tipos": ["Planta"]},
    254: {"nombre": "Sceptile", "tipos": ["Planta"]},
    255: {"nombre": "Torchic", "tipos": ["Fuego"]},
    256: {"nombre": "Combusken", "tipos": ["Fuego", "Lucha"]},
    257: {"nombre": "Blaziken", "tipos": ["Fuego", "Lucha"]},
    387: {"nombre": "Turtwig", "tipos": ["Planta"]},
    388: {"nombre": "Grotle", "tipos": ["Planta"]},
    389: {"nombre": "Torterra", "tipos": ["Planta", "Tierra"]},
    390: {"nombre": "Chimchar", "tipos": ["Fuego"]},
    391: {"nombre": "Monferno", "tipos": ["Fuego", "Lucha"]},
    392: {"nombre": "Infernape", "tipos": ["Fuego", "Lucha"]},
    495: {"nombre": "Snivy", "tipos": ["Planta"]},
    496: {"nombre": "Servine", "tipos": ["Planta"]},
    81: {"nombre": "Magnemite", "tipos": ["Acero", "Electrico"]},
    498: {"nombre": "Tepig", "tipos": ["Fuego"]},
    499: {"nombre": "Pignite", "tipos": ["Fuego", "Lucha"]},
    500: {"nombre": "Emboar", "tipos": ["Fuego", "Lucha"]},
    650: {"nombre": "Chespin", "tipos": ["Planta"]},
    651: {"nombre": "Quilladin", "tipos": ["Planta"]},
    652: {"nombre": "Chesnaught", "tipos": ["Planta", "Lucha"]},
    653: {"nombre": "Fennekin", "tipos": ["Fuego"]},
    654: {"nombre": "Zapdos", "tipos": ["Electrico","Volador"]},
    655: {"nombre": "Delphox", "tipos": ["Fuego", "Psíquico"]},
    722: {"nombre": "Rowlet", "tipos": ["Planta", "Volador"]},
    723: {"nombre": "Dartrix", "tipos": ["Planta", "Volador"]},
    448: {"nombre": "Lucario", "tipos": ["Lucha", "Acero"]},
    725: {"nombre": "Litten", "tipos": ["Fuego"]},
    726: {"nombre": "Torracat", "tipos": ["Fuego"]},
    727: {"nombre": "Incineroar", "tipos": ["Fuego", "Siniestro"]},
    810: {"nombre": "Grookey", "tipos": ["Planta"]},
    811: {"nombre": "Thwackey", "tipos": ["Planta"]},
    812: {"nombre": "Rillaboom", "tipos": ["Planta"]},
    813: {"nombre": "Scorbunny", "tipos": ["Fuego"]},
    814: {"nombre": "Raboot", "tipos": ["Fuego"]},
    815: {"nombre": "Cinderace", "tipos": ["Fuego"]},
    816: {"nombre": "Sobble", "tipos": ["Agua"]},
    817: {"nombre": "Drizzile", "tipos": ["Agua"]},
    818: {"nombre": "Raichu", "tipos": ["Electrico"]},
}

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

# Insertar Pokémon en los árboles
for numero, datos in pokemons.items():
    arbol_nombre.insert_node(datos["nombre"], datos)
    arbol_numero.insert_node(numero, datos)
    for tipo in datos["tipos"]:
        arbol_tipo.insert_node(tipo, datos)


#Punto b
def mostrar_pokemons_por_proximidad(nombre_parcial):
    pokemons_encontrados = arbol_nombre.proximity_search(nombre_parcial)
    if pokemons_encontrados:
        print(f"Pokémons que contienen '{nombre_parcial}':")
        for pokemon in pokemons_encontrados:
            tipos = ""
            for tipo in pokemon["tipos"]:
                tipos += tipo + ", "
            tipos = tipos[:-2] 
            print(f"Nombre: {pokemon['nombre']}, Tipo: {tipos}")
print("Pokémon que contienen 'Bul'")
mostrar_pokemons_por_proximidad("Bul")


#Punto c
def mostrar_pokemons_por_tipo(tipo_especifico):
    print(f"Pokémons de tipo '{tipo_especifico}':")
    for datos in pokemons.values():
        if tipo_especifico in datos["tipos"]:
            print(datos["nombre"])
mostrar_pokemons_por_tipo("Fuego")
mostrar_pokemons_por_tipo("Agua")
mostrar_pokemons_por_tipo("Planta")
mostrar_pokemons_por_tipo("Electrico")


#Punto d
def ordenar_por_nombre(pokemon):
    return pokemon["nombre"]
def listado_pokemons_ordenado():
    print("Listado de Pokémons en orden ascendente por número:")
    for numero in sorted(pokemons.keys()):
        print(f"Número: {numero}, Nombre: {pokemons[numero]['nombre']}")
    print("Listado de Pokémons en orden ascendente por nombre:")
    for nombre in sorted(pokemons.values(), key=ordenar_por_nombre):
        print(f"Nombre: {nombre['nombre']}")
listado_pokemons_ordenado()


#Punto e
def mostrar_datos_pokemons_especificos(nombres):
    print("Datos de los Pokémons específicos:")
    for nombre in nombres:
        for datos in pokemons.values():
            if datos["nombre"] == nombre:
                tipos = ""
                for tipo in datos["tipos"]:
                    tipos += tipo + ", "
                tipos = tipos[:-2]
                print(f"Nombre: {datos['nombre']}, Tipos: {tipos}")
mostrar_datos_pokemons_especificos(["Jolteon", "Lycanroc", "Tyrantrum"])


#Punto f
def contar_pokemons_por_tipo():
    contador_electrico = sum(1 for datos in pokemons.values() if "Electrico" in datos["tipos"])
    contador_acero = sum(1 for datos in pokemons.values() if "Acero" in datos["tipos"])
    print(f"Número de Pokémons de tipo Eléctrico: {contador_electrico}")
    print(f"Número de Pokémons de tipo Acero: {contador_acero}")
contar_pokemons_por_tipo()