# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 00:56:12 2020

@author: Giovanni
"""

from scipy.stats import binom 

#jogar uma moeda 5 vezes, qual a probabilidade de dar 3 caras? 
prob = binom.pmf(3,5,0.5)

# Passar por 4 sinais de 4 tempos, qual a probabilidade de pegar sinal verde 0,1,2,3,4 vezes seguidas?
binom.pmf(0,4,0.25)
binom.pmf(1,4,0.25)
binom.pmf(2,4,0.25)
binom.pmf(3,4,0.25)
binom.pmf(4,4,0.25)

# Probabilidade Acumulativa 
binom.cdf(4,4, 0.25)