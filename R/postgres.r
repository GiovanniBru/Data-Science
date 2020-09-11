library("RPostgreSQL")

# Primeiro precisamos fazer uma conexão: 
conexao = dbConnect("PostgreSQL", dbname="CursoCD", host="localhost", port=5432,
                    user="postgres", password=040604)
    # Usamos o dbConnect (database conexao) para conectar com postgres, parâmetros: 
      # "PostgreSQL" = tipo de conexão
      # dbname = nome da base de dados
      # host = localhost = seu computados
      # port = 5432 é a porta default 
      # user = usuário usado 
      # senha que criamos 

# Com a conexão feita podemos usar o objeto para rodar consultas SQL contra o banco de dados conectado
# Criamos uma variável para passar o comando: 
sql = "SELECT quantidade, valortotal, produto, total FROM itensvenda IV
        INNER JOIN vendas V on (IV.idvenda = V.idvenda)
        INNER JOIN produtos P on (IV.idproduto = P.idproduto)"
# Executando no banco de dados: 
vendas = dbGetQuery(conexao, sql)
print(vendas)

class(vendas) # data.frame