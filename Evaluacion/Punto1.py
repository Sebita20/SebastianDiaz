from random import randint

lista = []

for i in range(10):
    lista.append(randint(1,99))

print(lista)

def lista_inversa(lista):
    if len(lista) == 0:
        return []
    else:
        return lista_inversa(lista[1:]) + lista[:1]
print(lista_inversa(lista))