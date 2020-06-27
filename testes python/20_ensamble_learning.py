# -*- coding: utf-8 -*-
"""
Created on Tue May 26 21:17:05 2020

@author: Giovanni
"""

# Ensamble Learning: 
# utilizamos o algoritmo de Random Forest 
# usamos mais de um classificador
# Ele vai gerar várias árvores de decisão e analisa-las para tomar uma decisão 

# Copiado das aulas anteriores: 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score

credito = pd.read_csv('Credit.csv')
previsores = credito.iloc[:,0:20].values
classe = credito.iloc[:,20].values

labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:, 3] = labelencoder.fit_transform(previsores[:, 3])
previsores[:, 5] = labelencoder.fit_transform(previsores[:, 5])
previsores[:, 6] = labelencoder.fit_transform(previsores[:, 6])
previsores[:, 8] = labelencoder.fit_transform(previsores[:, 8])
previsores[:, 9] = labelencoder.fit_transform(previsores[:, 9])
previsores[:, 11] = labelencoder.fit_transform(previsores[:, 11])
previsores[:, 13] = labelencoder.fit_transform(previsores[:, 13])
previsores[:, 14] = labelencoder.fit_transform(previsores[:, 14])
previsores[:, 16] = labelencoder.fit_transform(previsores[:, 16])
previsores[:, 18] = labelencoder.fit_transform(previsores[:, 18])
previsores[:, 19] = labelencoder.fit_transform(previsores[:, 19])

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,
                                                                  classe,
                                                                  test_size = 0.3,
                                                                  random_state = 0)

from sklearn.ensemble import RandomForestClassifier

floresta = RandomForestClassifier(n_estimators = 100)
                                # n_estimators = numero de arvores que ele vai criar 
                                # para classificar ele vai usar o valor que mais 
                                # aparece entre os 100 resultados diferentes das árvores 
floresta.fit(X_treinamento, y_treinamento)

previsoes = floresta.predict(X_teste)

confusao = confusion_matrix(y_teste, previsoes)
taxa_acerto = accuracy_score(y_teste, previsoes)
# Taxa de acerto foi de 76%, dos algoritmos trabalhados ele nos deu o melhor valor 

# Visualizando detalhes sobre o algoritmo: 
floresta.estimators_ # Visualizamos as 100 arvores criadas 
floresta.estimators_[1] # Visualizando apenas 1 arvore 

