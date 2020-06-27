# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:50:20 2020

@author: Giovanni
"""

# Regressão linerar em Python 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

from sklearn.linear_model import LinearRegression 
    # Pacote de funções de Machine Learn 
    
base = pd.read_csv('cars.csv')
    # Cria a variável base com 3 atributos e 50 objetos 
    # O primeiro atributo é inutil, o segundo é a velocidade(speed) e o terceiro é a distancia(dist)
    # Distancia que o carro levou para parar em x velocidade 
    # Apagaremos o primeiro atributo pra facilitar: 
base = base.drop(['Unnamed: 0'], axis = 1)
    # axis=1 apagará por coluna 
    # .drop = função que apaga 
    # Agora temos apenas dois atributos 

    # Objetivo: Prever a velocidade que o carro estava pela distancia que demorou pra parar 
    # Precisamos criar uma variável X e uma Variável Y para jogar na função de Correlação 
X = base.iloc[:,1].values 
    # .values transforma pro formato necessário para correlação 
    # X será a variável independente, recebe a coluna 2 (1 pois começa em 0) que é a distancia
Y = base.iloc[:, 0].values
    # Y será a variável dependente, recebe a coluna 1(0) que é a velocidade 
    
    # Calculando a Correlação: 
correlacao = np.corrcoef(X,Y)
    # .corrcoef = coeficiente de correlação 
    # cria uma matrix com as correlações de X e Y 
    # A correlação será 0.8068, ou seja, é Forte 
    # Então podemos aplicar o modelo de Regressão Linear para prever

X = X.reshape(-1,1)
    # Transformação do X para array numpy, necessário pro .fit 

modelo = LinearRegression()
modelo.fit(X,Y)
    # .fit = encaixa os dados X e Y que devem estar em formato de array numpy 
    # método que faz o treinamento 
    
modelo.intercept_
    # mostra a interceptação 
modelo.coef_
    # mostra a inclinação 

plt.scatter(X,Y)
    # gera um gráfico dos dados
    # .scatter plota o gráfico 
plt.plot(X, modelo.predict(X), color ='red')
    # cria a linha de previsão
    # modelo.predict() passamos isso com a variável que queremos prever 
    
    # Testando a Previsão
    # Dist = 22 pés 
modelo.intercept_ + modelo.coef_ * 22
    # Previsão Manuel, feita com modelo já treinado 
modelo.predict(22)
    

    # AULA 2 
    
    # Para visualizar os residuais 
modelo._residues 
    
    # Biblioteca específica de Modelos de Machine Learning: 
    # Precisamos instalar no Prompt do Anaconda a biblioteca Yellowbrick 
    # pip install yellowbrick
from yellowbrick.regressor import ResidualsPlot 

visualizador = ResidualsPlot(modelo)
    # Objeto para visualização do Plot 
visualizador.fit(X,Y)
    # .fit fará o treinamento
visualizador.poof()

    # Será Criado um Gráfico com os valores dos Residuais 
    