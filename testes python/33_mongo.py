# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 02:25:44 2020

@author: Giovanni
"""

# pip install pymongo
from pymongo import MongoClient

# Criando conexão:
cliente = MongoClient('mongodb://localhost:27017/') # Podemos passar sem argumento ou com 

# Recuperando da conexão:
db = cliente.dbmidias

# Recuperando a coleção:
conexao = db.posts

print(conexao.find_one())
print(conexao.find_one({"nome":"José"}))

for conexao in conexao.find():
    print(conexao)