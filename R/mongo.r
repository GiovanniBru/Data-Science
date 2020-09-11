# install.packages("mongolite")

library(mongolite)

# Criando a conexão: 
conexao = mongo(collection="posts", db="dbmidias", url="mongodb://localhost")

# Recuperando os dados: 
dados = conexao$find()

class(dados)

dados = conexao$find('{"nome": "José"}')