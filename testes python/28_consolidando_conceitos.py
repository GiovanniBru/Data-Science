# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 01:18:19 2020

@author: Giovanni
"""

# Aula Bônus de consolidação de conceitos: 
# Vamos utilizar o arquivo Credit, porém uma versão diferente. 

# AULA 1 = PRÉ-PROCESSAMENTO

import pandas as pd

dataset = pd.read_csv("Credit2.csv", sep=";")

# Podemos observar os seguintes atributos desse arquivo:
    # ID - não será utilizada, deve ser ignorada
    # checking_status e credit_history =  variáveis categóricas 
    # várias variáveis numéricas
    # Classe = Good ou Bad

# Primeiramente precisamos separar as variáveis independentes da dependente 
# Depois precisamos transformar as variáveis categóricas em numéricas 
# Precisamos normalizar os dados
# e por último precisamos transformar a Classe 

# Separando as variáveis:
X = dataset.iloc[:,1:10].values
    # Pegamos todas as linhas, e as variáveis independentes de 1 a 9 (10 não entra pq é a classe, e 0 não entra pq é o ID)
Y = dataset.iloc[:, 10].values

# Pré-processamento de dados: 
    # Na primeira coluna usamos o Label Encoder (deixa só uma coluna com um número para cada valor)
    # Na segunda coluna usamos o One Hot Encoder (cria uma coluna binária para cada valor)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer 

labelencoder = LabelEncoder()
# Como são 4 valores na primeira coluna, devemos substitui-los por valores de 0 a 3 
X[:,0] = labelencoder.fit_transform(X[:,0])

# Como são 4 valores na segunda coluna, esperamos encontrar 5 novas colunas binárias com o OneHotEncoder
onehotencoder = make_column_transformer((OneHotEncoder(categories='auto', sparse=False), [1]), remainder='passthrough')
X = onehotencoder.fit_transform(X)

# Agora não temos mais variáveis categóricas 
# Porém temos o problema da dummy variable trap, por causa da alta correlação entre as variáveis criadas
# Para minimizar isso excluimos uma dessas colunas:
X = X[:,1:] # Eliminamos a coluna 0

# Agora transformamos a Classe em números usando o LabelEncoder
labelencoder_y = LabelEncoder()
Y = labelencoder_y.fit_transform(Y)

# AULA 2 = FUTURE-SCALING USANDO PADRONIZAÇÃO Z-SCORE

# Divisão do dados entre treino e teste:
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
# Foram separadas 800 linhas para treino e 200 para teste 

# Padronização Future-Scaling usando Z-Score
    # Equivalente a distribuição normal padrão = média 0 e desvio padrão 1
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# Agora podemos começar a criar a rede neural de fato:
from keras.models import Sequential 
from keras.layers import Dense 

classifier = Sequential()
classifier.add(Dense(units=6, kernel_initializer='uniform', activation='relu', input_dim=12))
classifier.add(Dense(units=6, kernel_initializer='uniform', activation='relu'))
classifier.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))
classifier.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])
classifier.fit(X_train, Y_train, batch_size=10, epochs=100)
# loss: 0.4626 - accuracy: 0.7850

# Fazendo Previsão: 
Y_pred = classifier.predict(X_test)
# Por usarmos o sigmoid, o resultado saiu em probabilidade
# Precisamos transformar a probabilidade em classificação:
Y_pred = (Y_pred>0.5)

# Medindo a acurácia do modelo: 
from sklearn.metrics import confusion_matrix 
cm = confusion_matrix(Y_test, Y_pred)
# Somando a diagonal da matriz de confusão temos: 24 + 119 = 143 acertos e 57 erros 

