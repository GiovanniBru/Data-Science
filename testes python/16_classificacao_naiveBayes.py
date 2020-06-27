# -*- coding: utf-8 -*-
"""
Created on Mon May 25 00:59:48 2020

@author: Giovanni
"""

# Classificação com Naive Bayes - Aula 1 = Tratamento de Dados 

import pandas as pd 
# Biblioteca de Machine Learning: 
from sklearn.model_selection import train_test_split 
                                    # Usamos essa função para divisão da base de dados entre treino e teste
from sklearn.naive_bayes import GaussianNB # NB = NaiveBayes
from sklearn.preprocessing import LabelEncoder 

credito = pd.read_csv('Credit.csv')

# Divisão da base dados: 
    # é necessário fazer uma variável que armazene as 20 variáveis independentes 
    # e outra com a Classe que é a variável dependente 
previsores = credito.iloc[:,0:20].values
                        # todas as linhas e colunas menos a 21 (vai de 0 a 19) 
classe = credito.iloc[:,20].values
                        # todas as linhas e apenas a linha 21 (começa do 0)

# Obs: o algoritmo GaussianNB não trabalha com dados categóricos 
    # Portanto precisamos fazer uma conversão, transformando tudo para valores numéricos
    # previsores[0][0]
    #  Out[19]: '<0'

labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
        #previsores[0][0]
        #Out[21]: 2

# Precisamos fazer isso com todos os atributos categoricos (os numericos, tipo o 1, nao precisa)
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

# Agora podemos passar essa base para o algoritmo GaussianNB 

X_treinamento, X_teste, Y_treinamento, Y_teste = train_test_split(previsores, classe, test_size=0.3, random_state=0)
#(dados[X recebe os previsores], classe[Y recebe a classe], tamanho do teste, random_state = para dividir a base de dados da mesma maneira)

# Aula 2 = Previsão 
                    
naive_bayes = GaussianNB()
naive_bayes.fit(X_treinamento, Y_treinamento) # Treinamento 

previsoes = naive_bayes.predict(X_teste)
        # Fazemos a previsão com os testes de X 
        # Agora comparamos com os testes de Y (classes) para contabilizar os acertos 
        
from sklearn.metrics import confusion_matrix, accuracy_score

confusao = confusion_matrix(Y_teste,previsoes)
    # Foi gerada uma tabela com os valores:
    # 41  45
    # 42  172
taxaAcerto = accuracy_score(Y_teste,previsoes)
    # Encontramos o valor de 0,71 ou 71% de acerto

# Visualizando a matriz de confusão melhor: 
from yellowbrick.classifier import ConfusionMatrix

v = ConfusionMatrix(GaussianNB())
v.fit(X_treinamento, Y_treinamento)
v.score(X_teste, Y_teste)
v.poof()

# Aula 3 = Simulando esse modelo em Produção 

novoCredito = pd.read_csv('NovoCredit.csv')

novoCredito = novoCredito.iloc[:,0:20].values
# Transformando pra numérico:

novoCredito[:,2] = labelencoder.fit_transform(novoCredito[:,2])
novoCredito[:, 3] = labelencoder.fit_transform(novoCredito[:, 3])
novoCredito[:, 5] = labelencoder.fit_transform(novoCredito[:, 5])
novoCredito[:, 6] = labelencoder.fit_transform(novoCredito[:, 6])
novoCredito[:, 8] = labelencoder.fit_transform(novoCredito[:, 8])
novoCredito[:, 9] = labelencoder.fit_transform(novoCredito[:, 9])
novoCredito[:, 11] = labelencoder.fit_transform(novoCredito[:, 11])
novoCredito[:, 13] = labelencoder.fit_transform(novoCredito[:, 13])
novoCredito[:, 14] = labelencoder.fit_transform(novoCredito[:, 14])
novoCredito[:, 16] = labelencoder.fit_transform(novoCredito[:, 16])
novoCredito[:, 18] = labelencoder.fit_transform(novoCredito[:, 18])
novoCredito[:, 19] = labelencoder.fit_transform(novoCredito[:, 19])

naive_bayes.predict(novoCredito)