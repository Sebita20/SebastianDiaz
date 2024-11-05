from grafo import Graph

personajes = ["Luke Skywalker", "Darth Vader",  "Han Solo", "Leia Organa", 
              "Obi-Wan Kenobi", "Boba Fett", "C-3PO", "Yoda"]

grafo = Graph(dirigido= False)

for personaje in personajes:
    grafo.insert_vertice(personaje)

grafo.insert_arista("Luke Skywalker", "Leia Organa", 3)
grafo.insert_arista("Luke Skywalker", "Darth Vader", 6)
grafo.insert_arista("Leia Organa", "Han Solo", 4)
grafo.insert_arista("Yoda", "Luke Skywalker", 2)
grafo.insert_arista("Chewbacca", "Han Solo", 4)
grafo.insert_arista("Han Solo", "Leia Organa", 3)
grafo.insert_arista("Han Solo", "Luke Skywalker", 2)

def Arbol_exp_min(Graph):
    Min = Graph.kruskal("Yoda")
    Está_yoda = any("Yoda" in camino for camino in Min)
    return Min, Está_yoda

grafo.show_graph()

Min, Está_yoda = Arbol_exp_min(grafo)
print("Árbol de expansión mínimo contiene a Yoda:", Está_yoda)

def max_episodios_compartidos(Graph):
    max_peso = 0
    for nodo in Graph.elements:
        for arista in nodo['aristas']:
            if arista['peso'] > max_peso:
                max_peso = arista['peso']
    return max_peso
max_peso = max_episodios_compartidos(grafo)
print(f"El número máximo de episodios que comparten dos personajes es: {max_peso}")

def arista_mas_grande(Graph):
    max_peso = 0
    nodos = (None, None)
    for nodo in Graph.elements:
        for arista in nodo['aristas']:
            if arista['peso'] > max_peso:
                max_peso = arista['peso']
                nodos = (nodo['value'], arista['value']) 
    return max_peso, nodos
peso_maximo, nodos_conectados = arista_mas_grande(grafo)
print(f"La arista más grande tiene un peso de {peso_maximo} y conecta a los nodos: {nodos_conectados[0]} y {nodos_conectados[1]}")