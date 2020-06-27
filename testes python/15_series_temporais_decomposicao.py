# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:43:08 2020

@author: Giovanni
"""
# Decompondo Series Temporais em Python 
import pandas as pd 
import numpy as np
import matplotlib.pylab as plt 

# Processo já visto anteriormente: 

base = pd.read_csv('AirPassengers.csv') 
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], 
                   index_col='Month', date_parser = dateparse)
ts = base['#Passengers']
          
plt.plot(ts)

# importação necessária para decomposição: 
from statsmodels.tsa.seasonal import seasonal_decompose 

decomposicao = seasonal_decompose(ts) # Decomposicao feita 

# Para visualizar: 
tendencia = decomposicao.trend # Cria a variavel de tendencia 
sazonal = decomposicao.seasonal # Cria a variavel de Sazonalidade 
aleatorio = decomposicao.resid # Cria a variavel com os aleatorios 
                        # Resid ve de residuo, seria o que sobrou tirando a tendencia e o sazonal 
plt.plot(sazonal)
plt.plot(tendencia)
plt.plot(aleatorio)

# Visualização de todos os gráficos juntos: 
plt.subplot(4,1,1)  # O ultimo numero escolhe a variavel (ID do indice)
                    # Tem que ser 4 em todos pois é o valor da COLUNA e temos 4 colunas 
                    # esse 1 no meio representa as LINHAS, por padrão é 1 
plt.plot(ts, label = 'Original') # label = nome 
plt.legend(loc='best') #.legend cria uma legenda, best = escolhe o melhor lugar pra ela 
        # Copio isso e colo 3 vezes: 
plt.subplot(4,1,2)
plt.plot(tendencia, label = 'Tendencia')
plt.legend(loc='best')

plt.subplot(4,1,3)
plt.plot(sazonal, label = 'Sazonalidade')
plt.legend(loc='best')

plt.subplot(4,1,4)
plt.plot(aleatorio, label = 'Aleatorio')
plt.legend(loc='best')

plt.tight_layout() # Funcao para melhorar a visualização 