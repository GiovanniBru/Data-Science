# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:21:59 2020

@author: Giovanni
"""

# Seleção de Atributos em Python 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score

# Funções copiadas da tarefa anteriro: 

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

# Seleção de Atributos: 
    # Vamos criar um modelo com todos os atributos e um com apenas os melhores atributos e comparar o resultado 
    
from sklearn.svm import SVC 
# svm = select vector machine 

svm = SVC()
svm.fit(X_treinamento, y_treinamento)

previsoes = svm.predict(X_teste)
taxa_acerto = accuracy_score(y_teste, previsoes)
    # A taxa de acerto foi de 71%
    
from sklearn.ensemble import ExtraTreesClassifier 

forest = ExtraTreesClassifier()
forest.fit(X_treinamento, y_treinamento)

importancias = forest.feature_importances_
    # é criada uma variavel que mostra a importancia de cada atributo 
    # os maiores valores são o 1, 2, 5
X_treinamento2 = X_treinamento[:,[0,1,4]]
X_teste2 = X_teste[:,[0,1,4]]

svm2 = SVC()
svm2.fit(X_treinamento2, y_treinamento)
previsoes2 = svm2.predict(X_teste2)

taxa_acerto2 = accuracy_score(y_teste, previsoes2)
# Taxa de acerto foi igual a anterior 

# Outro teste: 

X_treinamento3 = X_treinamento[:,[0,1,2,3]]
X_teste3 = X_teste[:,[0,1,2,3]]

svm3 = SVC()
svm3.fit(X_treinamento3, y_treinamento)
previsoes3 = svm3.predict(X_teste3)
taxa_acerto3 = accuracy_score(y_teste, previsoes3)

# Essa taxa de acerto foi um pouco menor que as outras 
