# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 23:08:59 2020

@author: Giovanni
"""

# Regras de Associação com Apriori 

import pandas as pd 

#instala-se o pacote: 
#pip install apyori

from apyori import apriori 

dados = pd.read_csv('transacoes.txt', header=None)

# para utilizar o pacote precisamos fazer uma codificacao manual no dataframe 
transacoes = []
for i in range(0,6):
    transacoes.append([str(dados.values[i,j])for j in range(0,3)])
    
# Minerando as regras:
regras = apriori(transacoes, min_support=0.5, min_confidence=0.5)

resultado = list(regras)

# Codificação para visualizar melhor as regras: 
resultados2=[list(x) for x in resultado]

resultados3 = []
for j in range(0,7):
    resultados3.append([list(x) for x in resultados2[j][2]])