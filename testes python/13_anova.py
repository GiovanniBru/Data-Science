# -*- coding: utf-8 -*-
"""
Created on Tue May 12 20:31:59 2020

@author: Giovanni
"""

# Anova em Python 

import pandas as pd
from scipy import stats 

tratamento = pd.read_csv('anova.csv', sep=';')
# Variável de Resposta = horas 

tratamento.boxplot(by='Remedio')
    # Fazemos o bloxplot para observar os dados 
    # Observamos que a concentração do Remédio A é mais centra, do B é mais pra baixo, e do C mais pra cima 
    
import statsmodels.api as sm 
from statsmodels.formula.api import ols 
    # Importação do método de regressão necessário, parecido com R  
   
# Teste para um Fator     
modelo1 = ols('Horas ~ Remedio', data=tratamento).fit()
resultados1 = sm.stats.anova_lm(modelo1)
    # Dentro dessa variável encontramos o valorP = 0,59 e comparamos com o Alfa 

# Teste de Dois Fatores
modelo2 = ols('Horas ~ Remedio * Sexo', data=tratamento).fit()
resultados2 = sm.stats.anova_lm(modelo2)
    # Encontramos 3 valores de P, comparação entre os remédios 

# Se, observando esses dados, concluimos que há variação, para descobrir onde está a variação usamos Tukey
from statsmodels.stats.multicomp import MultiComparison 

mc = MultiComparison(tratamento['Horas'], tratamento['Remedio'])
resultadoTeste = mc.tukeyhsd()
print(resultadoTeste)

resultadoTeste.plot_simultaneous()