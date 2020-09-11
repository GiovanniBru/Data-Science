# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:14:30 2020

@author: Giovanni
"""

# pip install psycopg2
import psycopg2 

# Primeiro é preciso fazer a conexão: 
conexao = psycopg2.connect(host="localhost", database="CursoCD", user="postgres", password="XXXX")
    # é opcional passar a porta, se não passar ela vai a padrão (5432)
    
# Precisamos agora criar um CURSOR para percorres os dados
cursor = conexao.cursor()

# Agora podemos consultar: 
consulta = "SELECT * FROM clientes"

# Executamos o cursor: 
cursor.execute(consulta)

# Agora executamos um método para retornar os registros e armazenar numa variável: 
registros = cursor.fetchall()
    # fetchall = retorna todos os registros e armazena em registros 

# Imprimindo alguns registros: 
for row in registros:  # row = linhas 
    print("Nome=", row[1]) # row[1] = primeiro parâmetro que é o nome, pulamos o 0 pq não queremos ver o ID
    print("Estado=", row[2]) 
    print("Status=", row[4], "\n") 

# Podemos fechar o cursor e a conexao: 
cursor.close()
conexao.close()