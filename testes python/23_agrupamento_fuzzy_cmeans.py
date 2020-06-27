# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:30:29 2020

@author: Giovanni
"""

# Agrupamento com Fuzzy c-means 
# Esse tipo de algoritmo pode definir que os registros podem fazer parte de mais de um grupo
# Agrupamento Parcial Difuso 
# Como resultado temos a probabilidade de cada registro pertencer a cada grupo

from sklearn import datasets 
import numpy as np
from sklearn.metrics import confusion_matrix 
import skfuzzy
    # pip install scikit-fuzzy

iris = datasets.load_iris()

resultado = skfuzzy.cmeans(data=iris.data.T, c=3, m=2, error=0.005,
                           maxiter=1000, init=None)
                                    # .T = Transpõe a matriz = linha vira coluna e coluna vira linha
                                    # c=3 = numero de clusters 
                                    # m, error, maxiter e init são valores default, padrão

previsoes_porcentagem = resultado[1]    
    # a posição 1 do resultados é onde fica as porcentagens e agora separamos ela

previsoes_porcentagem[0][0]                              
    # Out[16]: 0.002304457475406935 = probabilidade de estar no grupo 0 

# Verificando o quanto o algoritmo acertou: 
previsoes = previsoes_porcentagem.argmax(axis=0)    
resultados = confusion_matrix(iris.target, previsoes)
    # Ao somar vemos que teve 16 erros 