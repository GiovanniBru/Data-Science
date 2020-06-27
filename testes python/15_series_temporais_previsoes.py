# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:55:08 2020

@author: Giovanni
"""

# Previsão de Séries Temporais em Python 

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

# A maneira mais fácil de fazer uma previsão é utilizando a média:
ts.mean()
    # Out[15]: 280.2986111111111
    # Porém a chance de erro é enorme, por causa da tendencia 
# Um pouco mais preciso é pegar a média apenas do último ano: 
ts['1960-01-01':'1960-12-01'].mean()
    # Out[16]: 476.1666666666667

# Médias Móveis: considerano N elementos antes para fazer a média 
media_movel = ts.rolling(window=12).mean()
    # temos os dados das médias móveis com alguns valores 'nan' que são nulos 

ts[0:12].mean() # Encontramos o valor que ta na primeira posição da variável 
    # Out[18]: 126.66666666666667
ts[1:13].mean() # Encontramos o valor que ta na segunda posição da variável 
    # Out[19]: 126.91666666666667
    
    # se botarmos o window = 1 não muda da média móvel pra base normal 
    
plt.plot(ts) # Grafico Normal 
plt.plot(media_movel,color='red') # Gráfico da média móvel 
    # Podemos observar que o gráfico da média móvel começa depois pois não pega os 12 primeiros meses ja que so faz a soma com 12 meses antes
    
# Usando a Média Móvel para Prever: DE MANEIRA MANUAL 
previsoes = []
for i in range(1,13):
    superior = len(media_movel) - i
    inferior = superior - 11
    #print(inferior)
    #print(superior)
    #print('----')
    previsoes.append(media_movel[inferior:superior].mean())

previsoes = previsoes[::-1] # Instrucao de Inversao 

plt.plot(previsoes)