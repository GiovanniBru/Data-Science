# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 23:28:05 2020

@author: Giovanni
"""

# AULA 4 - Impressão de grafos com igraph 
from igraph import Graph
from igraph import plot

grafo5 = Graph(edges = [(0,1),(2,3),(0,2),(0,3)], directed = True)
grafo5.vs['label'] = ['Fernando', 'Pedro', 'Jose', 'Antonio']
grafo5.vs['peso'] = [40,30,30,25]
grafo5.es['TipoAmizade'] = ['Amigo', 'Inimigo', 'Inimigo', 'Amigo']
grafo5.es['weight'] = [1,2,1,3]

# Visualizando os vértices e arestas:
for v in grafo5.vs:
    print(v)
    
for e in grafo5.es:
    print(e)

plot(grafo5, bbox=(300,300))

# Imprimindo o vértice de acordo com o tamanho (peso)
plot(grafo5, bbox=(300,300), vertex_size=grafo5.vs['peso'])

# Imprimindo com base nas arestas:
plot(grafo5, bbox=(300,300), vertex_size=grafo5.vs['peso'],
     edge_width = grafo5.es['weight'])

# Mudando a cor dos vértices: 
grafo5.vs['cor'] = ['blue', 'red', 'yellow', 'green']
plot(grafo5, bbox=(300,300), vertex_size=grafo5.vs['peso'],
     edge_width = grafo5.es['weight'], vertex_color = grafo5.vs['cor'])

# Mudando o formato dos vértices: 
plot(grafo5, bbox=(300,300), vertex_size = grafo5.vs['peso'],
     edge_width = grafo5.es['weight'],
     vertex_color = grafo5.vs['cor'],
     edge_curved = 0.4, vertex_shape = 'square')
    # edge_curved = deixa a aresta curva 

