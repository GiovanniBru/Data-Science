# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:10:42 2020

@author: Giovanni
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression 

base = pd.read_csv('mt_cars.csv')   #Criacao da base de dados
base = base.drop(['Unnamed: 0'], axis=1) # Remoção de atributo inútil 

# Inicialmente faremos uma correlação entre o consumo e as polegadas (Regressão Simples)
# mpg = consumo por galão; disp = polegadas do motor 

X = base.iloc[:, 2].values # Variável Independente 
Y = base.iloc[:, 0].values # Variável Dependente 

correlacao = np.corrcoef(X,Y)
    # Correlacao deu -0,84 = Correlação negativa (um aumenta o outro diminui) e Forte

# Precisamos fazer o reshape da variável Independente 
X = X.reshape(-1,1)
    # -1 significa que não vou mexer nas linhas 
    # 1 significa que vou adicionar mais uma coluna 
    # X vira uma matriz 
    
modelo = LinearRegression()
modelo.fit(X,Y)
    # Modelo de previsão criado com sucesso 
    
    # Visualização dos parâmentros: 
modelo.intercept_
    # Out[6]: 29.59985475616395
modelo.coef_
    # Out[7]: array([-0.04121512])
    
# Coeficiente de Dispersão R²: 
modelo.score(X,Y)
    # Out[8]: 0.7183433404897299
    
# Coeficiente de Dispersão Ajustado: 
    # Precisamos de uma nova biblioteca
previsoes = modelo.predict(X)
    # Essa variável contem os valores que meu modelo fez a previsão para cada um deles
    # Esses valores são comparáveis com seu Y, a diferença entre eles seria os Residuais 

import statsmodels.formula.api as sm 
    # Biblioteca que serve para gerar modelos no Python como se estivesse criando códigos em R 
    # Pois no Python as vezes é dificil visualizar alguns dados
    
modelo_ajustado = sm.ols(formula = 'mpg ~ disp', data = base)
modelo_treinado = modelo_ajustado.fit()
modelo_treinado.summary()
    # Na saída veremos vários dados igual no R 
    # R-squared = 0,71
    # R-squared Ajustado = 0,709

# Visualização do Gráfico: 
plt.scatter(X,Y)
plt.plot(X, previsoes, color='red')
    
# Previsão: 
modelo.predict(200) 

# Regressão Linear Multipla 

X1 = base.iloc[:, 1:4].values 
    # Vamos prever o consumo baseado nos atributos: cyl, disp e hp
Y1 = base.iloc[:, 0].values 

modelo2 = LinearRegression()
modelo2.fit(X1,Y1)

modelo2.score(X1,Y1)
    # Out[18]: 0.7678877440928638
    # Isso mostra a Correlação da variável Dependente com as Independentes 
modelo_ajustado2 = sm.ols(formula = 'mpg ~ cyl + disp + hp', data = base)
modelo_treinado2 = modelo_ajustado2.fit()
modelo_treinado2.summary()
    #  R-squared:  0.768
    # Adj. R-squared:  0.743

novo = np.array([4,200,100])
    # 4 = cyl; 200 = disp; 100 = hp
    # Precisamos transformar a variável 
novo.reshape(1,-1)
    # 1 = adiciona uma linha
    # -1 = nao mexe na coluna 
    
modelo2.predict(novo)