# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 03:42:21 2020

@author: Giovanni
"""

# Grafos com Igraph - AULA 1 

# Primeiramente precisamos instalar os pacotes no prompt:
# pip install pycairo - pacote de visualização dos grafos 
# pip install python-igraph 

from igraph import Graph
from igraph import plot 
import matplotlib.pyplot as plt 

#Criando o primeiro grafo:
grafo1=Graph(edges=[(0,1),(1,2),(2,3),(3,0)], directed=True)
print(grafo1)
# 0->1 1->2 2->3 3->0

#plotando o grafo:
# plot(grafo1)
# Plotando com janela menor:
plot(grafo1, bbox = (300,300))

# Como definir os nomes para cada vértice: 
grafo1.vs['label'] = range(grafo1.vcount())
plot(grafo1, bbox = (300,300))
    # vs = significa que é um atributo de cada vértice
    # .vcount() = indica quantos vértices nos temos 
    # range() = mostra uma contagem = range(0,4)
    # essa função diz que o grafo 1 vai receber do 0 ao 3 as nomeações 

# Criando outros grafos: 
grafo2 = Graph(edges = [(0,1),(1,2),(2,3),(3,0),(0,3),(3,2),(2,1),(1,0)], directed = True)
grafo2.vs['label'] = range(grafo2.vcount())
plot(grafo2, bbox = (300,300))

# Exemplo com auto-relacionamento: 
grafo3 = Graph(edges = [(0,1),(1,2),(2,3),(3,0),(1,1)], directed = True)
grafo3.vs['label'] = range(grafo3.vcount())
plot(grafo3, bbox = (300,300))

grafo4 = Graph(edges = [(0,1),(1,2),(2,3),(3,0),(1,1)], directed = True)
grafo4.add_vertex(5)
    # Como adicionar um novo vértice num gráfico já construido 
grafo4.vs['label'] = range(grafo4.vcount())
plot(grafo4, bbox = (300,300))

# o vértice está desconectado do grafo pois nao fizemos nenhuma conexao no Graph 

