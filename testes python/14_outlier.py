# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:52:20 2020

@author: Giovanni
"""

# Outlier em Python 

import matplotlib.pyplot as plt 
import pandas as pd 

iris = pd.read_csv('iris.csv')

# Procuraremos os outliers no atributo Speal Width 

# Utiliando um boxplot 
plt.boxplot(iris.iloc[:,1])
    # Analisando o boxplot gerado encontramos 3 outliers superiores e 1 inferior 
plt.boxplot(iris.iloc[:,1], showfliers=True)
    # Geramos um boxplot sem os outliers 
    
# Para extrair esses 4 outliers: 
outliers = iris[(iris['sepal width']>4.0)]
outliersInf = iris[(iris['sepal width']>4.0) | (iris['sepal width']< 2.1)]

# Biblioteca de detecção de Outlier: PyOD 
# pip install pyod 
from pyod.models.knn import KNN 

sepal_width = iris.iloc[:,1]
# Transformacao necessaroa:
sepal_width = sepal_width.reshape(1,-1)
detector = KNN()
detector.fit(sepal_width)

previsoes = detector.labels_
    # Cria uma variável com valores 0 e 1, onde tem 1 existe outlier 