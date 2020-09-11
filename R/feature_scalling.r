# Feature Scalling = dimensionamento de categoria 
# Vamos transformar dados do conjunto Iris, padronizando e depois normalizando 

# Gerando o boxplot do iris sem transformação nenhuma: 
boxplot(iris[,1:4])
  # Vamos que eles estão em escalas diferentes 

# Primeiro fazemos a padronização (Z-Score)
iris_padr = scale(iris[,1:4])
            # Função nativa do R 
            # O conjunto iris foi padronizado para uma escala normal 
boxplot(iris_padr)
            # vemos que agora os dados estão distribuidos de forma padronizada 

# Normalização (com min e max)
normaliza = function(x){
  return((x-min(x))/(max(x)-min(x)))
}

iris_norm = normaliza(iris[,1:4])
boxplot(iris_norm)
    # A normalização transformou todos os valores entre 0 e 1 
    # O padrão da distribuições é mantido, porém os valores são transformados 
