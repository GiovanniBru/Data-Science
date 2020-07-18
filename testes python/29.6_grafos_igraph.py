# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 00:25:18 2020

@author: Giovanni
"""

# Aula 6 - Caminhos e Distâncias com igraph
from igraph import Graph
from igraph import plot

grafo = Graph(edges = [(0,2),(0,1),(1,4),(1,5),(2,3),(6,7),(3,7),(4,7),(5,6)],
                       directed = True)
grafo.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
grafo.es['weight'] = [2,1,2,1,2,1,3,1]

# Colocando em cada aresta o valor da distância: 
plot(grafo, bbox = (300,300), edge_label = grafo.es['weight'])

# Descobrir a menor rota entre A e H: 
caminho_vertice = grafo.get_shortest_paths(0,7, output = 'vpath')
    # índice 0 = A; índice 7 = H
    # output = vpath =  cria uma lista com o caminho na saída
# Para visualizar o nome do vértice ao invés do índice:
for n in caminho_vertice[0]: 
    #print(n)
    print(grafo.vs[n]['label'])

# com 'epath' retorna as arestas que foram visitadas
caminho_aresta = grafo.get_shortest_paths(0,7, output = 'epath')

# Codificação para retornar o valor da distância: 
caminho_aresta_id = [] 
for n in caminho_aresta[0]:
    caminho_aresta_id.append(n)
# O formato é o mesmo, mas mudou a estrutura. Antes tinhamos uma lista agora temos um vetor simples
# Foi feita essa transformação manual para percorrer esses indices mais facilmente quando for fazer o somatório:
distancia = 0
for e in grafo.es:
    #print(e.index)
    if e.index in caminho_aresta_id: # Se o id da aresta tiver no caminho:
        distancia += grafo.es[e.index]['weight']
    
# Segunda Aula = Impressão do caminho no grafo: 

caminho_nome_vertices = []
for n in caminho_vertice[0]:
    print(grafo.vs[n]['label'])
    caminho_nome_vertices.append(grafo.vs[n]['label']) # Preenche a lista com os nomes 
    # Caminho : A->B, B->E, E->H

# Vamos fazer um for para pintar os vértices que estão na lista:
for v in grafo.vs:
    if v['label'] in caminho_nome_vertices:
        v['color'] = 'green'
    else:
        v['color'] = 'gray'

# For para pintar as arestas que estão na lista: 
for e in grafo.es:
    if e.index in caminho_aresta_id:
        e['color'] = 'green'
    else:
        e['color'] = 'gray'

plot(grafo, bbox = (300,300), edge_label = grafo.es['weight'])

