# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:16:26 2020

@author: Giovanni
"""

from scipy.stats import norm 

# Conjunto de objetos em uma cesta, a média é 8kg e o desvio padrão é 2

# Qual a probabilidade de tirar um objeto que o peso é menor que 6kg? 

norm.cdf(6,8,2)
# cdf = usada quando queremos um < (menor que)
# norm.cdf(Valor que procuramos, Media, DP)

# Qual a probabilidade de tirar um ojeto que o peso é maior que 6kg?
norm.sf(6,8,2)
# SF = survivor function = usado quando queremos um > (maior que)
# norm.sf(Valor que procuramos, Media, DP)

# Outra maneira de mudar de > pra < (ou vice-versa)
1 - norm.cdf(6,8,2)

# Qual a probabilidade de tirar um objeto que o peso é menor que 6 ou maior que 10kg?
norm.cdf(6,8,2) + norm.sf(10,8,2)

# Qual a probabilidade de tirar um objeto que o peso é menor que 10 e maior que 8kg?
norm.cdf(10,8,2) - norm.sf(8,8,2)

