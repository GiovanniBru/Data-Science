# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:33:26 2020

@author: Giovanni
"""

# Feature Scalling em Python

import pandas as pd 
from sklearn.preprocessing import StandardScaler, MinMaxScaler

dataset = pd.read_csv("Credit.csv")

# Queremos agora trabalhar com colunas numéricas (coloridas)
# Seram as colunas 1, 4 e 7 

dt = dataset.iloc[:, [1,4,7]].values 

# Padronização - Z-Score: 
sc = StandardScaler()
x = sc.fit_transform(dt)
# As 3 variaveis foram padronizadas: centralizadas em 0 e com desvio padrão 1 

# Normalização com MinMax 
sc = MinMaxScaler()
y = sc.fit_transform(dt)
# Os 3 valores estão entre 0 e 1 
