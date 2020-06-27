# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:12:36 2020

@author: Giovanni
"""

import numpy as np
from scipy import stats
        #scipy = biblioteca de funções estatísticas
        
jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]

np.mean(jogadores)

np.median(jogadores)

quartis = np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1])
                                    #precisamos especificar a posição dos quartis 
                                    
np.std(jogadores) #calculo do Desvio Padrao

#No Desvio Padrão é calculado em Python com N, em R é com N-1, 
# Para ajustar isso precisamos adaptar a função para:

np.std(jogadores, ddof=1)

#Para visualizar os dados: 

stats.describe(jogadores) #apresenta vários dados 