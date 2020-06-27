# -*- coding: utf-8 -*-
"""
Created on Mon May 11 21:20:35 2020

@author: Giovanni
"""

# Regressão Logística em Python 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

from sklearn.linear_model import LogisticRegression

base = pd.read_csv('Eleicao.csv', sep=';')

# Vamos gerar um gráfico das despesas x situacao 
plt.scatter(base.DESPESAS, base.SITUACAO)

base.describe()
np.corrcoef(base.DESPESAS, base.SITUACAO)
# Correlacao = 0.81 = Positiva e Forte 
# Criaremos as variáveis de Situacao e Despesa 
X = base.iloc[:,2].values # Variavel Independente 
X = X[:,np.newaxis]     # newaxis vai criar uma nova coluna 
Y = base.iloc[:,1].values # Variavel Independente 

modelo = LogisticRegression()
modelo.fit(X,Y)
# Modelo criado e treinado
modelo.coef_
# Out[9]: array([[0.00298895]])
modelo.intercept_
# Out[10]: array([-2.41847443])

# Veremos agora o gráfico de previsões 
X_test = np.linspace(10,3000, 100) 
    # Essa funcao cria 100 valores aleatorios entre 10 e 3000
    
def model(x):
    return 1/(1+np.exp(-x)) # Essa funcao receberá um número e retornará sua função segmoide
r = model(X_test * modelo.coef_ + modelo.intercept_).ravel()
    # r = resultado 
    # .ravel = transforma o numpy array de matriz para vetor 
    # Essa funcao calcula o Erro que a matriz ta gerando 
plt.plot(X_test, r, color='red')
    # Criará um gráfico com a curva de probabilidade 
    
# Agora faremos as previsões com o arquivo de novos candidatos
base_previsoes = pd.read_csv('NovosCandidatos.csv', sep=';')
despesas = base_previsoes.iloc[:,1].values
despesas = despesas.reshape(-1,1)
previsoes_teste = modelo.predict(despesas)
base_previsoes = np.column_stack((base_previsoes, previsoes_teste))