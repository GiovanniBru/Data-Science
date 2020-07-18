# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 21:03:23 2020

@author: Giovanni
"""

# Grafos com Igraph AULA 3
from igraph import Graph
from igraph import plot

# Codificação da aula anterior: 
grafo4 = Graph(directed = False)
grafo4.add_vertices(5)
grafo4.add_edges([(0,1),(1,2),(2,3),(3,4),(4,0),(0,2),(2,1)])
grafo4.add_vertex(5)
grafo4.add_vertex(6)
grafo4.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Como renomear os vértices: 
grafo4.vs['name'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# Visualizando a matriz de adjacência: 
print(grafo4.get_adjacency())
grafo4.get_adjacency()[0,]
# Out[10]: [0, 1, 1, 0, 1, 0, 0]
grafo4.get_adjacency()[0,1]
# Out[11]: 1
# Como visualizar o nome dos grafos: 
for v in grafo4.vs:
   print(v) 

plot(grafo4, bbox=(300,300))

# Novo grafo com nomes de pessoas: 
grafo5 = Graph(edges = [(0,1),(2,3),(0,2),(0,3)], directed = True)
grafo5.vs['label'] = ['Fernando', 'Pedro', 'Jose', 'Antonio']
    # Adicionando um valor para cada vértice:
grafo5.vs['peso'] = [40,30,30,25]
    # Para visualizar se os pesos foram atribuidos: 
for v in grafo5.vs:
    print(v)
# Acessando o valor individualmente:
grafo5.vs[0] # Vemos os dados apenas do Fernando

# Assim como fizemos um FOR para ver os vértices, podemos fazer para as arestas:
for e in grafo5.es:  # es = edges; vs = vertices
    print(e)
    # Podemos ver a ligação entre os vértices, mas não vemos nada atribuido a elas
# Adicionando um nome a essa ligação entre pessoas:
grafo5.es['TipoAmizade'] = ['Amigo', 'Inimigo', 'Inimigo', 'Amigo']
    # Agora executando o FOR conseguimos observar o tipo de relação
# Visualizando individualmente: 
grafo5.es[0]
# Acessando um único atributo especifico: 
grafo5.es['TipoAmizade']

# Podemos também passar o peso das arestas:
grafo5.es['weight'] = [1,2,1,3]
print(grafo5) # Observa-se que adicionou a letra W pois agora é um grafo ponderado

# Adicionando um TIPO para o grafo:
grafo5.vs['type'] = 'Humanos'
# Agora executando o print percebemos que adicionou a letra T, pois é um grafo com tipo

# Nomeando o grafo: 
grafo5['name'] = 'Amizades'

plot(grafo5, bbox=(300,300))