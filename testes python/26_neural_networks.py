# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 00:03:06 2020

@author: Giovanni
"""

# Neural Network na Prática 
from sklearn import datasets 
from sklearn.model_selection import train_test_split
from yellowbrick.classifier import ConfusionMatrix
# iremos usar a base de dados iris e a biblioteca keras, portanto precisamos instalar o tensor flow
# pip install tensorflow
# tensorflow é o framework de deeplearning feito pelo google, o keras roda dentro dele
# pip install keras
from keras.models import Sequential #chamada do modelo sequencial 
from keras.layers import Dense # camada densa = todos os neuronios estao conectados entre si
from keras.utils import np_utils # utilidades usadas 

base = datasets.load_iris()

#dividindo a base de dados:
previsores = base.data
classe = base.target

classe_dummy = np_utils.to_categorical(classe)
# isso indica que a camada de saida terá 3 neurônios, pois temos 3 opções na classe 

