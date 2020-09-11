library(mltools)
library(data.table)

tit = as.data.frame(Titanic)
      # Convers�o dos dados do Titanic para data frame 

# Label Encoding: vamos transformar as 3 primeiras categorias (Class, sex, age)

labenc = data.matrix(tit[,1:3])
      # Fun��o nativa do R que passa os dados para matrix j� fazendo o label encoding

# One-Hot Encoding: com os mesmos atributos vamos 

hotenc = one_hot(as.data.table(tit[,1:3]))
        # Fun��o que faz o OneHot
        # Ela recebe um data.matrix e transforma para data.table novamente 
