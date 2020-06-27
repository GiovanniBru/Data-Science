# -*- coding: utf-8 -*-
"""
Created on Mon May 25 01:43:50 2020

@author: Giovanni
"""

# Arvore de Decisao em Python 

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

# Começando: 
from sklearn.tree import DecisionTreeClassifier

arvore = DecisionTreeClassifier()
arvore.fit(X_treinamento, y_treinamento)
    # Foi gerada uma arvore de decisao
    # Para visualizar precisamos instalar um pacote: 
    # pip install graphviz
import graphviz
from sklearn.tree import export_graphviz

export_graphviz(arvore, out_file='tree.dot')
                        # out_file = arquivo de saida 
                        # foi criado um arquivo chamado tree.dot
                        # copiamos os dados do arquivo
                        # entramos no site webgraphviz.com 
                        # colamos e geramos o grafico 
                        
# Agora para fazer as previsões: 
                        
previsoes = arvore.predict(X_teste) 
# Agora precisamos comparar o previsto com o Y_teste 
confusao = confusion_matrix(y_teste, previsoes)
taxa_acerto = accuracy_score(y_teste, previsoes)
# O valor da taxa de acerto foi 0,68 ou 68%

