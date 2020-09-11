# Feature Scalling = dimensionamento de categoria 
# Vamos transformar dados do conjunto Iris, padronizando e depois normalizando 

# Gerando o boxplot do iris sem transforma��o nenhuma: 
boxplot(iris[,1:4])
  # Vamos que eles est�o em escalas diferentes 

# Primeiro fazemos a padroniza��o (Z-Score)
iris_padr = scale(iris[,1:4])
            # Fun��o nativa do R 
            # O conjunto iris foi padronizado para uma escala normal 
boxplot(iris_padr)
            # vemos que agora os dados est�o distribuidos de forma padronizada 

# Normaliza��o (com min e max)
normaliza = function(x){
  return((x-min(x))/(max(x)-min(x)))
}

iris_norm = normaliza(iris[,1:4])
boxplot(iris_norm)
    # A normaliza��o transformou todos os valores entre 0 e 1 
    # O padr�o da distribui��es � mantido, por�m os valores s�o transformados 
