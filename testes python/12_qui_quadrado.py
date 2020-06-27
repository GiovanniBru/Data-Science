# -*- coding: utf-8 -*-
"""
Created on Tue May 12 20:26:43 2020

@author: Giovanni
"""

# Qui Quadrado em Python

from scipy.stats import chi2_contingency 
import numpy as np 

# Criaremos a base de dados da novela 
novela = np.array([[19,6],[43,32]])

# Teste:
chi2_contingency(novela)
#Out[4]: 
#    (2.037351443123939, 0.15347667161786666, 1, array([[15.5,  9.5],
#        [46.5, 28.5]]))

# Valor de p obtido: 0,15
# Maior que o Alfa padrão (0,05) então a hipótese é aceita 