# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:16:22 2020

@author: Giovanni
"""

# Distribuição de Poisson em Python 

from scipy.stats import poisson 

# Média de acidentes de carro é 2 por dia 

# Qual a probabilidade de ocorrer 3 acidentes no dia? 
poisson.pmf(3,2)
    # (x, lambda)
    # Out[2]: 0.18044704431548356
    
# Qual a probabilidade de ocorrer 3 ou menos no dia? 
poisson.cdf(3,2)
    # Quando for menos usamos CDF 
    # Out[3]: 0.857123460498547
    
# Qual a probabilidade de ocorrer mais de 3 no dia? 
poisson.sf(3,2)
    # Quando for mais usamos SF
    # Out[4]: 0.14287653950145296 