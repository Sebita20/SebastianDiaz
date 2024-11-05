from Cola import Queque
Cola_jedis = Queque()

jedis = [
    {'nombre': 'Ahsoka Tano', 'maestros': ['Anakin Skywalker'], 'colores_sable': ['verde', 'blanco'], 'especie': 'Togruta'},
    {'nombre': 'Kit Fisto', 'maestros': ['Mace Windu'], 'colores_sable': ['verde'], 'especie': 'Nautolan'},
    {'nombre': 'Yoda', 'maestros': [], 'colores_sable': ['verde'], 'especie': 'Desconocido'},
    {'nombre': 'Luke Skywalker', 'maestros': ['Yoda', 'Obi-Wan Kenobi'], 'colores_sable': ['azul'], 'especie': 'Humano'},
    {'nombre': 'Mace Windu', 'maestros': ['Yoda'], 'colores_sable': ['violeta'], 'especie': 'Humano'},
    {'nombre': 'Qui-Gon Jinn', 'maestros': [], 'colores_sable': ['verde'], 'especie': 'Humano'},
    {'nombre': 'Obi-Wan Kenobi', 'maestros': ['Qui-Gon Jinn'], 'colores_sable': ['azul'], 'especie': 'Humano'},
    {'nombre': 'Aayla Secura', 'maestros': ['Ki-Adi-Mundi'], 'colores_sable': ['verde'], 'especie': 'Twi\'lek'},
    {'nombre': 'Barriss Offee', 'maestros': ['Luminara Unduli'], 'colores_sable': ['verde'], 'especie': 'Mirialan'},
]

for jedi in jedis:
    Cola_jedis.arrive(jedi)

print("Lista ordenada de los jedis por nombre:")
jedi_ordenados = []
for i in range(Cola_jedis.size()):
    jedi_ordenados.append(Cola_jedis.attention())
for i in sorted(jedi_ordenados, key=lambda x: (x['nombre'], x['especie'])):
    print(f"Nombre: {i['nombre']}, Especie: {i['especie']}")

print("----------------------------------")
print("Informacion sobre Ahsoka Tano y Kit Fisto ")
for i in jedi_ordenados:
    if i['nombre'] in ['Ahsoka Tano', 'Kit Fisto']:
        print(f"Nombre: {i['nombre']}, Maestros: {i['maestros']}, Colores de sable: {i['colores_sable']}, Especie: {i['especie']}")

print("----------------------------------")
print("Padawans de Yoda y Luke Skywalker")
padawans = []
for i in jedi_ordenados:
    if 'Yoda' in i['maestros'] or 'Luke Skywalker' in i['maestros']:
        padawans.append(i['nombre'])
for padawan in padawans:
    print(f"Padawans: {padawan}")

print("----------------------------------")
print("Los Jedi de especie humana y Twi'lek son: ")
for i in jedi_ordenados:
    if i['especie'] in ['Humano', "Twi'lek"]:
        print(f"Nombre: {i['nombre']}, Especie: {i['especie']}")

print("----------------------------------")
print("jedis que comienzan con la letra A:")
for i in jedi_ordenados:
    if i['nombre'].startswith('A'):
        print(f"Nombre: {i['nombre']}")

print("----------------------------------")
print("jedis que que pueden usar mas de un color de sable:")
for i in jedi_ordenados:
    if len(i['colores_sable']) > 1:
        print(f"Nombre: {i['nombre']}, Colores de sable: {i['colores_sable']}")