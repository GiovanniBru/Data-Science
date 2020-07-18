# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:51:04 2020

@author: Giovanni
"""
# Reconhecimento dos dígitos manuscritos utilizando deep learning e a biblioteca keras
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import np_utils
import numpy as np
from sklearn.metrics import confusion_matrix
from keras.datasets import mnist

(X_treinamento, y_treinamento), (X_teste, y_teste) = mnist.load_data()
    # carregando as variáveis diretamente do mnist 
    # são 10.000 imagens de teste, todas 28x28 e 60.000 imagens de treinamento
    # o y mostra o número que cada variável representa 

#visualizando um exemplo:
plt.imshow(X_treinamento[1])
# visualizamos o 0 
plt.imshow(X_treinamento[2], cmap='gray')
# cmap='gray' visualizamos a imagem em escala de cinza
plt.title(y_treinamento[2])
# rodando o titulo ao mesmo tempo que  imagem vemos a corretude da rede 

# Precisamos fazer alguns pré-processamentos para aplicar a rede neural
# Primeiramente fazemos um reshape para mudar o formato: 
X_treinamento = X_treinamento.reshape((len(X_treinamento), np.prod(X_treinamento.shape[1:])))
X_teste = X_teste.reshape((len(X_teste), np.prod(X_teste.shape[1:])))
# Ao executar isso, mudamos o formato para ao invés de 28x28 aparecer 784 
    # np.prod faz essa multiplicacao de 28x28

#Agora precisamos transformar os valores de inteiro para float 
X_treinamento = X_treinamento.astype('float32')
X_teste = X_teste.astype('float32')
# é necessário fazer essa transformação para aplicar a normalização dos dados 
# pois se continuasse com valores entre 0 e 255 o algoritmo teria mais trabalho
# Normalização: 
X_treinamento /= 255
X_teste /= 255
# tudo ficou numa escala entre 0 e 1 

# último pré-processamento: mudar o padrão dos dados da variável y para o tipo dummy:
y_treinamento = np_utils.to_categorical(y_treinamento, 10)
y_teste = np_utils.to_categorical(y_teste, 10)
# 10 é o número de classes (do 0 ao 9)
# agora ficou tudo em binário

# AULA 2

# Iniciando a criação da rede neural:
modelo = Sequential() # Inicialização do modelo em camadas sequenciais 
# adicionando as camadas:
modelo.add(Dense(units = 64, activation = 'relu', input_dim = 784))
    # units = neuronios da primeira camada 
    # função de ativação = relu = boa para procesamento de imagens
    # input_dim = número de neuronios da camada de entrada 
modelo.add(Dropout(0.2)) 
    # Essa camada serve para que zeremos algumas entradas, quando temos muitos neuronios na camada de entrada
    # evita o overfitting 
    # 0,2 = 20%, dos 64 neuronios ele zera 20% enquanto estiver fazendo o treinamento 
modelo.add(Dense(units = 64, activation = 'relu'))
modelo.add(Dropout(0.2))
modelo.add(Dense(units = 64, activation = 'relu'))
modelo.add(Dropout(0.2))
modelo.add(Dense(units = 10, activation = 'softmax'))
    # Camada de saída = units = 10 pois é o número de classes (do 0 a 9)
    # função de ativação = softmax = retorna uma probabilidade de ser cada um dos numeros 

modelo.summary() #visualizando a rede 

# Compilando a rede: 
modelo.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
historico = modelo.fit(X_treinamento, y_treinamento, epochs = 20, validation_data = (X_teste, y_teste))

# Visualizando informações sobre o treinamento: 
historico.history.keys()
# mostra os valores que podemos acessar 
# Out[15]: dict_keys(['val_loss', 'val_accuracy', 'loss', 'accuracy'])
# accuracy = acuracia
# loss = erro na base de dados 

#plotando um gráfico com esses valores:
plt.plot(historico.history['val_loss'])
plt.plot(historico.history['val_accuracy'])

# Fazendo previsões:
previsoes = modelo.predict(X_teste)
# Matriz de confusão:
y_teste_matriz = [np.argmax(t) for t in y_teste]
y_previsoes_matriz = [np.argmax(t) for t in previsoes]
confusao = confusion_matrix(y_teste_matriz, y_previsoes_matriz)

# Agora que o modelo está gerado, vamos fazer um teste de previsão:
y_treinamento[20] # Executando essa linha vemos que deu o número 4
novo = X_treinamento[20] # atribui os pixels do 20 na variavel novo
novo = np.expand_dims(novo, axis = 0)
    # função de ajuste do novo para deixar com apenas 1 linha e 784 atributos 
pred = modelo.predict(novo)

