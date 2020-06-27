# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:11:52 2020

@author: Giovanni
"""

from scipy.stats import t 
    # Biblioteca de importação do T Student 

# Ex: Média = 75 ; Amostra n = 9 ; DP = 10
# Qual a probabilidade de selecionar um cientista de dados e o salário ser menor que 80?

t.cdf(1.5,8)
    # t.cdf(T , grau de liberdade ou n-1)
    
# Qual a probabilidade do salário ser maior que 80?
t.sf(1.5,8)