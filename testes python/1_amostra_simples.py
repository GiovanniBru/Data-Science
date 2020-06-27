# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 02:09:32 2020

@author: Giovanni
"""

#TESTE AMOSTRAGEM ALEATÓRIA 

import pandas as pd
import numpy as np #biblioteca com funcoes estatisticas

base = pd.read_csv('iris.csv')

base

base.shape

amostra = np.random.choice(a=[0,1], size=150, replace=True, p = [0.5, 0.5])

len(amostra)
len(amostra[amostra==1])
len(amostra[amostra==0])

np.random.seed(2345)
amostra = np.random.choice(a=[0,1], size=150, replace=True, p = [0.5, 0.5])

len(amostra)
len(amostra[amostra==1])
len(amostra[amostra==0])