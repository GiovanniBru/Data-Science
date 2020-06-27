# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:45:50 2020

@author: Giovanni
"""

from scipy import stats 
from scipy.stats import norm
import matplotlib.pyplot as plt 
# matplotlib é uma das melhores bibliotecas de importação de gráficos 

dados = norm.rvs(size=100)
# rvs é uma função para gerar dados na distribuição normal

stats.probplot(dados,plot=plt)
# (array de dados, biblioteca de geração do gráfico)
# Será gerado um gráfico na saída e verificando-o percebemos que é uma Distribuição Normal

stats.shapiro(dados)
# Realização do teste de shapiro-will