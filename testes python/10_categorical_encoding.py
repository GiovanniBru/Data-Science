# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:18:00 2020

@author: Giovanni
"""

# Categorical Encoding em Python 

import pandas as pd 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer

dataset = pd.read_csv("Credit.csv")

# Vamos testar com o atributo "personal_status" que tem 4 valores diferentes 
# e "other_parties" que tem 3 valores diferentes 
# Eles são os indices 8 e 9 

x = dataset.iloc[:, 8:10].values # O python ignora o ultimo valor (10)

# Label Encoding  na primeira coluna 
labelencoder = LabelEncoder()
x[:,0] = labelencoder.fit_transform(x[:,0])

# OneHot Encoder na segunda coluna 
onehotencoder = make_column_transformer((OneHotEncoder(categories='auto', sparse=False),
                                         [1]), 
                                        remainder="passthrough")
                                    
X = onehotencoder.fit_transform(x)
