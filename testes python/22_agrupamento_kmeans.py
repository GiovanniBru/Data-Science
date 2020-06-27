# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:11:46 2020

@author: Giovanni
"""
# Agrupamento com K-Means

from sklearn import datasets 
import numpy as np 
from sklearn.metrics import confusion_matrix 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

iris = datasets.load_iris()

# Contagem de elementos que temos de cada classe:
unicos, quantidade = np.unique(iris.target, return_counts=True)

# Agora vamos utilizar o algoritmo de agrupamento para comparar com esse agrupamento original 

cluster = KMeans(n_clusters = 3)
                # n_clusters = numero de grupos
cluster.fit(iris.data)

# Para vermos alguns resultados: 
centroide = cluster.cluster_centers_
    # Na variavel centroide vemos onde ficou o centro de cada uma das medidas
previsoes = cluster.labels_
    # Nessa variavel previsoes vemos 150 instancias e quais grupos eles pertencem 

unicos2, quantidade2 = np.unique(previsoes, return_counts=True)
    # Observamos que o quantidade2 que era pra conter 3 grupos com 50 50 50
    # tinha 3 grupos com 50 62 38, ou seja ele classificou 12 erroneamente 

resultados = confusion_matrix(iris.target, previsoes)

plt.scatter(iris.data[previsoes==0,0], iris.data[previsoes==0,1],
            c='green', label='Setosa')
    # previsoes==0 so pegamos os que foram classificados como 0, pegamos da coluna 0 e da 1 
    # c = cor no grafico, label = nome 
plt.scatter(iris.data[previsoes==1,0], iris.data[previsoes==1,1],
            c='red', label='Versicolor')
plt.scatter(iris.data[previsoes==2,0], iris.data[previsoes==2,1],
            c='blue', label='Virginica')
plt.legend() # Adiciona Legenda 