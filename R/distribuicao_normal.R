install.packages("sampling")
library(sampling)
amostraIris = strata(iris, c("Species"), size=c(25,25,25), method="srswor")
summary(amostraIris)
infert
summary(infert)
120 / 248 * 100
amostra1 = strata(infert, c("education"), size=c(5,48,47), method="srswor")
summary(amostra1)
amostra1
install.packages("TeachingSampling")
library(TeachingSamples)
library(TeachingSampling)
amostra = S.SY(150,10)
amostra
amostrairis1 = iris[amostra,]
amostrairis1
q()
jogadores = c(40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000)
mean(jogadores)
median(jogadores)
quartis = quantile(jogadores)
quartis 
quartis[4]
sd(jogadores) 
summary(jogadores)
q()
#media = 8, dp = 2, qual a probabilidade de tirar um objeto q o pesado seja menor que 6kg? 
pnorm(6,8,2)
#media = 8, dp = 2, qual a probabilidade de tirar um objeto q o pesado seja maior q 10kg? 
#media = 8, dp = 2, qual a probabilidade de tirar um objeto q o pesado seja mais que 6kg? 
pnorm(6,8,2, lower.tail=F)
#ou podemos calcular assim:
1 - pnorm(6,8,2)
#qual a chance de tirar um objeto com menos de 6kg e mais de 10kg?
 #qual a chance de tirar um objeto com menos de 6kg OU mais de 10kg?
pnorm(6,8,2) + pnorm(10,8,2, lower.tail=F)
#Qual a chance de tirar um objeto com menos de 10kg e mais de 8kg?
pnorm(10,8,2) - pnorm(8,8,2)
