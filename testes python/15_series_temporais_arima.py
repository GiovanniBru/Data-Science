# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:04:38 2020

@author: Giovanni
"""

# Previsão de Séries Temporais em Python com ARIMA 

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

# Previsões para o futuro: Extrapolar o conjunto de dados

 # Importação do ARIMA 
 from statsmodels.tsa.arima_model import ARIMA 
 
 modelo = ARIMA(ts, order=(2,1,2))
     # ORDER = 3 parâmetros: order=(p,q,d)
            # p = número dos termos autoregressivos 
            # q = número da média movel 
            # d = número de diferenças não-sazonais 
        # Como encontrar esses valores de p q e d vemos la embaixo (autoarima)
modelo_treinado = modelo.fit()

modelo_treinado.summary()
    # Verificação dos parametros encontrados pro modelo 

previsoes = modelo_treinado.forecast(steps=12)
        # steps = quantas previsões para frente eu desejo fazer 
        # a primeira posição do array gerado "previsoes[0]" é as previsoes de verdade
previsoesREAIS = modelo_treinado.forecast(steps=12)[0]

# Para gerar um gráfico com as previsões: 
eixo = ts.plot()
modelo_treinado.plot_predict('1960-01-01', '1962-01-01',
                             ax=eixo, plot_insample=True)
                             #ax = eixo = une os dois gráficos
    # No gráfico: 
        # Azul = Previsões originais 
        # laranja = Forecast 
        # verde = previsão do mes que ja temos
        # cinza = intervalo de confiança                      
    
eixo = ts.plot()
modelo_treinado.plot_predict('1960-01-01', '1970-01-01',
                             ax=eixo, plot_insample=True)
        # Nesse gráfico bem futuro podemos observar que a linha vai ficando mais linear
        # perdendo a sazonalidade, e o intervalo de confiança sempre aumenta 
    
# Para trabalhar com o auto-arima: 
# Utilizamos o pacote PMDARIMA
# pip install pmdarima

from pmdarima.arima import auto_arima
import pmdarima as pm 

# Usamos o autoarima para definir os parametros do p,q e d

modelo_auto = auto_arima(ts, n=12, seasonal=True, trace=True)
    # n=12 é a distribuição mensal da nossa série 
modelo_auto.summary()
    # no sumário vemos quais os melhores parametros que o autoarima encontrou
    # SARIMAX(2, 1, 2) p=2, q=1, d=2
    
# ANTES de fazer o modelo temos que fazer esse autoarima para encontrar esses parametros 
    
# Previsão com AutoArima: 
proximos_12 = modelo_auto.predict(n_periods=12)
    # n_periods = numero de periodos 
# Os valores gerados são um POUQUINHO diferentes da previsao anterior 
