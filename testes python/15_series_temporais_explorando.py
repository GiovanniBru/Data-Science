# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:34:34 2020

@author: Giovanni
"""

# Explorando Séries Temporais em Python 
import pandas as pd 
import numpy as np
import matplotlib.pylab as plt 

base = pd.read_csv('AirPassengers.csv') 

# Processo necessário para trabalhar com Serie Temporal em python: 
print(base.dtypes)
    # print que mostra os tipos das variáveis 
    # Month          object
    # Passengers     int64
    # o mês é objeto e passageiros é int
    # precisamos transformar o tipo object em tipo data se não não conseguiremos trabalhar com série temporal
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
    # essa função do pandas .strptime pega o objeto e transforma em data 
    # % indica que tem números, Y é Year, M é Months 
base = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], 
                   index_col='Month', date_parser = dateparse)
    # Agora a variável tem 144 linhas e 1 coluna 
    # a única coluna é o número de passageiros e seu índice é a Data completa 
    
base.index
    # Mostra os índices no console 
    
# Agora precisamos mudar o tipo 'DataFrame' para um tipo 'Series'
ts = base['#Passengers']
    # ts = time series
ts[1]
    # nos mostra o valor do íncide 1 = Out[8]: 118
ts['1949-02']
    # os mostra todos os passageiros do mes 2 de 1949
    
# Outra maneira de indexar: 
from datetime import datetime 
ts[datetime(1949,2,1)]
   # Out[16]: 118
   
# Indexação por intervalos: 
ts['1950-01-01':'1950-07-31']
    # Nos mostrara todos os passageiros do mes 1 ao 7 
ts[:'1950-07-31']
    # Mostra todos os passageiros até o mes 7 de 1951
ts['1950']   
    # Mostra todos os meses de 1950

# Para saber o maior valor: 
ts.index.max()  
    # Out[20]: Timestamp('1960-12-01 00:00:00')
ts['1960-12-01']
    # Out[21]: 432 = o valor máximo é 432
    
# Para saber o valor mínimo: 
ts.index.min()
    # Out[22]: Timestamp('1949-01-01 00:00:00')
ts['1949-01-01']
    # Out[23]: 112
    
# Visualização do gráfico total:
plt.plot(ts)

# Agrupamento por ano: 
ts_ano = ts.resample('A').sum()
    # cria uma nova séria com 12 anos e seus valores somados, sum() faz a soma 
plt.plot(ts_ano)
    # gráfico mostrando o ano é linearmente crescente pois perdemos a sazonalidade 

# Agrupamento por mês: 
ts_mes = ts.groupby([lambda x: x.month]).sum()
    # cria uma nova séria com 12 registros dos meses agrupados 
plt.plot(ts_mes)
    # podemos visualizar que há um crescimento nos meses 6,7,8 que representam o verão americano 
    
# Gráfico filtrando por datas: 
ts_datas = ts['1960-01-01':'1960-12-01']
    # cria uma variavel com os dados apenas do ano 1960
plt.plot(ts_datas)