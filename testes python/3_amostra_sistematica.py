# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 03:01:40 2020

@author: Giovanni
"""

import numpy as np
import pandas as pd

from math import ceil 

populacao = 150
amostra = 15
k = ceil(populacao/amostra)

#pra definir a aleatoriedade 
r = np.random.randint(low = 1, high = k+1, size =1)

acumulador = r[0]

sorteados = []

for i in range(amostra):
    #print(acumulador)
    sorteados.append(acumulador)
    acumulador += k
    
base = pd.read_csv('iris.csv')
base_final = base.loc[sorteados]