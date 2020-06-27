# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 22:25:52 2020

@author: Giovanni
"""

# Agrupamento com algoritmo K-medoids 
# esse algoritmo escolhe pontos reais ja existentes na base de dados 

#pip install pyclustering

from sklearn import datasets
from sklearn.metrics import confusion_matrix
import numpy as np
from pyclustering.cluster.kmedoids import kmedoids 
from pyclustering.cluster import cluster_visualizer

iris = datasets.load_iris()

# nos vamos trabalhar com o agrupamento dos atributos 0 e 1 
# pois essa função de visualização so nos permite ver dois atributos 

cluster = kmedoids(iris.data[:,0:2], [3,12,20])
                    # dados[todas as linhas, colunas 0 e 1 ]
                    # [3,12,20] = initial_index_medoid = indice dos pontos na base de dados q vamos utilizar para indexação
                        # é comum usar pontos aleatórios mesmo, nao faz muita diferença 
cluster.get_medoids() 
    # Out[21]: [3, 12, 20]                 
cluster.process()
    # a função process faz o treinamento, ou melhor, o agrupamento 
previsoes = cluster.get_clusters()

medoids = cluster.get_medoids()
    # encontramos os pontos 7, 67 e 112, que são nossos verdadeiros medoids 

#Visualização do cluster:
v = cluster_visualizer()
v.append_clusters(previsoes, iris.data[:,0:2])
v.append_cluster(medoids, iris.data[:,0:2], marker='*', markersize=15) # para marcar com estrela onde estão os medoids 
v.show()

# Comparativo para ver os acertos: 
    # Precisamos fazer uma coficação manual para conseguir gerar uma variavel no padrão do iris.target
    # para conseguir usar a confusion_matrix:
lista_previsoes = []
lista_real = []
for i in range(len(previsoes)):
    print('-----')
    print(i)
    print('-----')
    
    for j in range(len(previsoes[i])):
        #print(j)
        print(previsoes[i][j])
        lista_previsoes.append(i) 
        lista_real.append(iris.target[previsoes[i][j]])
        
# Transformando essas duas listas pro formato do numpy array
lista_previsoes = np.asarray(lista_previsoes)
lista_real = np.asarray(lista_real)

resultados = confusion_matrix(lista_real, lista_previsoes)
    # contabilizamos 26 erros 