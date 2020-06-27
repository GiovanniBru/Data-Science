# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:35:28 2020

@author: Giovanni
"""

# Aprendizado Baseado em instância = KNN 

from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix, accuracy_score 

from sklearn.neighbors import KNeighborsClassifier # Biblioteca do KNN
from sklearn import datasets # Biblioteca com várias bases de dados imbutidas 
from scipy import stats # para visualizar estatisticas 

# Vamos utilizar a base de dados das plantas 
iris = datasets.load_iris()
stats.describe(iris.data) # visualizacao dos dados da iris 

previsores = iris.data # armazena os atributos 
classe = iris.target # numeros 1 2 e 3 que significam os tipos de plantas 

# Dividindo treinamento e teste: 
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,
                                                                  classe,
                                                                  test_size=0.3,
                                                                  random_state=0)

knn = KNeighborsClassifier(n_neighbors = 3) # Numero de vizinhos escolhidos = 3 
knn.fit(X_treinamento, y_treinamento)
# Nesse tipo de algoritmo, o treinamento armazena os valores 
# e quando chega um novo valor para classificar 
# ele faz a comparação da distancia com os registros armazenados 

previsoes = knn.predict(X_teste)  

# Agora comparamos as previsoes com o Y_teste 

confusao = confusion_matrix(y_teste, previsoes)
# os acertos estão na diagonal principal, percebemos que só há 1 erro
taxa_acerto = accuracy_score(y_teste, previsoes)
# Taxa de acerto = 97%
