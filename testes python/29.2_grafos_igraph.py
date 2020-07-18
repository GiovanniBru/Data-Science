# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:38:28 2020

@author: Giovanni
"""

# Grafos com igraph 

from igraph import Graph
from igraph import plot

grafo1 = Graph(edges = [(0,1),(2,2),(2,3),(3,0)], directed = True)
grafo1.vs['label'] = range(grafo1.vcount())
print(grafo1)

# Entendendo a saída: 
# IGRAPH D--- 4 4 --       - tipo=IGRAPH; D=Direcionado; 4=numero de vértices;4=número de arestas

grafo2 = Graph(edges = [(0,1),(2,2),(2,3),(3,0)], directed = False)
print(grafo2)
# IGRAPH U--- 4 4 --       - U = grafo não direcionado

# Criando um grafo vazio e adicionando as arestas depois: 
grafo3 = Graph(directed = False)
grafo3.add_vertices(10) # Função de adicionar 10 vértices
grafo3.add_vertex(16) # Adiciona mais um vértice individual
print(grafo3)
# IGRAPH U--- 10 0 --       - 10 vértices e nenhuma aresta
plot(grafo3) # Foi plotado 10 vértices isolados 
grafo3.add_edges([(0,1),(2,2),(2,3),(3,0)]) #Adicionando as arestas
plot(grafo3, bbox=(300,300))

# Exemplo de como colocar caracteres:
grafo4 = Graph(directed = False)
grafo4.add_vertices(5)
grafo4.add_edges([(0,1),(1,2),(2,3),(3,4),(4,0),(0,2),(2,1)])
grafo4.add_vertex(5)
grafo4.add_vertex(6)
grafo4.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# O programa vai adicionando os labels de acordo com a ordem que o numero aparece na função .add_edges 
plot(grafo4, bbox=(300,300))
