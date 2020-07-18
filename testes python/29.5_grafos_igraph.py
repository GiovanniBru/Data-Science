# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 23:35:35 2020

@author: Giovanni
"""

# Aula 5 - Métricas 
from igraph import Graph
from igraph import plot
import igraph

# Vamos carregar um arquivo especifico para construção de grafos:
grafo = igraph.load('Grafo.graphml')

print(grafo)

plot(grafo, bbox = (300,300))

# Descobrindo o grau do grafo: 
grafo.degree(type = 'all') # tanto de entrada quanto de saída 
grafo.degree(type = 'in') # só de entrada
grafo.degree(type = 'out') # só de saída 

# Colocando o tamanho do vértice de acordo com a quantidade de entrada:
grau = grafo.degree(type = 'in') # No caso do exemplo, isso mostra quantas pessoas seguem esse usuario
plot(grafo, vertex_size = grau)

# Testes com o diâmetro do grafo: 
grafo.diameter(directed = False)
    # Na saida foi 5
grafo.diameter(directed = True)
    # Na saida foi 8
# Isso é usado para medir qual é a maior distância entre os vértices,
    # com o direcionado temos mais limites, por isso o valor é maior
    
#Retorna os vértices que tem a maior distância entre os pontos do grafo
grafo.get_diameter()

# Visualizando a vizinhança: 
grafo.neighborhood()

# Testando se dois grafos são isomorfos:
grafo2 = grafo
grafo.isomorphic(grafo2) 
