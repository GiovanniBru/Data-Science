# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:24:31 2020

@author: Giovanni
"""

# Dashboards em Python 

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as srn 

base = pd.read_csv('trees.csv')

# Histograma 
h = np.histogram(base.iloc[:,1], bins = 'auto')
    # bins = auto = cria altomaticamente o número de colunas do histograma, também podemos defini-los como um numero qualquer 
plt.hist(base.iloc[:,1])
    # Printa o histograma 
    # Podemos adicionar o número de bins 
    # plt.hist(base.iloc[:,1], bins = 6)
# Configurando propriedades: 
plt.title('Árvores')
plt.ylabel('Frequencia')
plt.xlabel('Altura')    

# Densidade 

srn.distplot(base.iloc[:,1])
    # Mostra o gráfico de densidade com uma linha mostrando o caminho 
# Podemos passar alguns parâmetros adicionais: 
srn.distplot(base.iloc[:,1], hist=False)
    # hist = False não mostra o histograma 
srn.distplot(base.iloc[:,1], hist=False, kde=False)
    # kde = false não mostra o gráfico de densidade 
srn.distplot(base.iloc[:,1], hist=True, kde = True, bins = 6, 
             color = 'red', hist_kws={'edgecolor':'black'} )
                                        # edgecolor = coloca divisão nas barras do histograma 

# Dispersão 
        # Utilizado para ver se tem correlação entre variáveis contínuas 
plt.scatter(base.Girth, base.Volume) # Scatter cria um plano cartesiano e passamos os dados de X e Y
plt.title('árvores')
plt.xlabel('Volume')
plt.ylabel('Circunferencia')

# Personalizações: 
plt.scatter(base.Girth, base.Volume, color='blue', facecolors='none', marker='*') 
plt.title('árvores')                            # facecolor = tira o preenchimento 
plt.xlabel('Volume')                            # marker = muda o desenho 
plt.ylabel('Circunferencia')

plt.plot(base.Girth, base.Volume) # plt.plot = passa uma linha nos pontos 

# Evitando sobreposições de valores próximos: 
# Gerando ruído randomico uniforme 
srn.regplot(base.Girth, base.Volume, data=base) # Gera um gráfico já com uma linha de regressão 
# adicionando um ruído no eixo x: 
srn.regplot(base.Girth, base.Volume, data=base, x_jitter=0.3, fit_reg=False)
                                                                # fit_reg=False tira a linha de regressão
            # Esse parâmetro só altera a visualização, não muda os dados 

# Dispersão com Legendas 
            # Variáveis categóricas com numéricas 
base2 = pd.read_csv('co2.csv')
x = base2.conc
y = base2.uptake

# Buscando os nomes das categorias: 
unicos = list(set(base2.Treatment))
            # set = pega os valores sem repeti-los
for i in range(len(unicos)):
    indice = base2.Treatment == unicos[i]
    # Variável booleana que recebe TRUE ou FALSE de acordo com a condicão (base.treatment = unicos[i])
    plt.scatter(x[indice], y[indice], label = unicos[i])
plt.legend(loc = 'lower right')


# Divisão da Tela 

plt.figure(1)
    # figure = cria uma nova figura para criar um conjunto de gráficos 
# Primeiro gráfico = girth com volume 
plt.subplot(2,2,1)
    # subplot = primeiro parâmetro = número de linhas 
                # Segundo parâmetro = número de colunas 
                # Terceiro parâmetro = valor do gráfico 
plt.scatter(base.Girth, base.Volume)

# Segundo Gráfico = girth com height 
plt.subplot(2,2,2)
plt.scatter(base.Girth, base.Height)

# Terceiro Gráfico = height com volume 
plt.subplot(2,2,3)
plt.scatter(base.Volume, base.Height)

# Quarto Gráfico = histograma do volume 
plt.subplot(2,2,4)
plt.hist(base.Volume)

# Todos os gráficos estão dentro da figura 1 


# Boxplot 
plt.boxplot(base.Volume)
# Configurando parâmetros: 
plt.boxplot(base.Volume, vert=False, showfliers= False, notch = True )
    # vert = false, bota na horizontal 
    # showfliers=false, tira os outliers
    # notch = true, achata na mediana 
plt.boxplot(base.Volume, vert=False, showfliers= False, notch = True, 
            patch_artist = True) # patch_artist muda a cor
plt.title('Arvores')
plt.xlabel('Volume')

# Opcões para colorir: 
# https://matplotlib.org/gallery/statistics/boxplot_demo.html

# Boxplot para todas as variáveis: 
plt.boxplot(base) # Gera vários boxplots juntos, difícil de entender 

plt.boxplot(base.Volume, vert=False)
plt.boxplot(base.Girth, vert=False)
plt.boxplot(base.Height, vert=False)
    # Executando todos juntos ficam sobrepostos e ruins de ler 
    # O ideal é dividir a tela com subplot para mostrar todos os boxplots 
    

# Gráfico de Barras e Setores
    # Uteis para mostrar variáveis categóricas e quando é preciso sumarizar os valores 
base3 = pd.read_csv('insect.csv')

# Primeiramente precisamos fazer um agrupamento de todos os valores nas categorias: 
agrupado = base3.groupby(['spray'])['count'].sum()
        # groupby = função do pandas que faz o agrupamento 
        # primeiro parâmetro = categoria 
        # segundo parâmetro = dados somados 
        # .sum faz a soma 
# Agora podemos fazer os gráficos 
agrupado.plot.bar(color = 'gray')

agrupado.plot.pie(legend=True)


# Boxplot com Seaborn 
srn.boxplot(base.Volume).set_title('Arvores')

srn.boxplot(data=base) # boxplot com todos os atributos 

# Histograma e Densidade com Seaborn 

srn.distplot(base.Volume, bins = 10, axlabel='Volume').set_title('Arvores')

base4 = pd.read_csv('chicken.csv')

agrupado2 = base4.groupby(['feed'])['weight'].sum()

# Geração dos Graficos do histograma com a densidade para cada um dos tipos de alimentação 
teste = base4.loc[base4['feed']=='horsebean']

plt.figure()
plt.subplot(3,2,1)
srn.distplot(base4.loc[base4['feed']=='horsebean'].weight).set_title('horsebean')
                                                    # .weight = atributo que quero criar o histograma
plt.subplot(3,2,2)
srn.distplot(base4.loc[base4['feed']=='casein'].weight).set_title('casein')

plt.subplot(3,2,3)
srn.distplot(base4.loc[base4['feed']=='linseed'].weight).set_title('linseed')

plt.subplot(3,2,4)
srn.distplot(base4.loc[base4['feed']=='meatmeal'].weight).set_title('meatmeal')

plt.subplot(3,2,5)
srn.distplot(base4.loc[base4['feed']=='soybean'].weight, hist = False).set_title('soybean')
                                                # hist = False tira o histograma 
plt.subplot(3,2,6)
srn.distplot(base4.loc[base4['feed']=='sunflower'].weight).set_title('sunflower')
plt.tight_layout() # melhorando a visualização 


# Mais gráficos de Dispersão com Seaborn: 
    # Vamos usar a base 2 de co2
srn.scatterplot(base2.conc, base2.uptake, hue=base2.Type)
    # scatterplot plota em eixo X e Y, precisamos primeiramente passar os eixos
    # hue = colore os pontos de acordo com a categoria passada e legenda automaticamente 

# Gráfico de dispersão condicional: 
    # Precisamos dividir os dados
q = base2.loc[base2['Type'] == 'Quebec'] # Separou só os Quebec
m = base2.loc[base2['Type'] == 'Mississippi']

plt.figure()
plt.subplot(1,2,1)
srn.scatterplot(q.conc, q.uptake).set_title('Quebec')
plt.subplot(1,2,2)
srn.scatterplot(m.conc, m.uptake).set_title('Mississippi')
plt.tight_layout()

# Dividindo entre refrigerado e não refrigerado
ch = base2.loc[base2['Treatment'] == 'chilled']
nc = base2.loc[base2['Treatment'] == 'nonchilled']

plt.figure()
plt.subplot(1,2,1)
srn.scatterplot(ch.conc, ch.uptake).set_title('Chilled')
plt.subplot(1,2,2)
srn.scatterplot(nc.conc, nc.uptake).set_title('Non chilled')
plt.tight_layout()

# Explorando o relacionamento entre variáveis categóricas 
base5 = pd.read_csv('esoph.csv')

srn.catplot(x='alcgp', y='ncontrols', data=base5, jitter=False)
    # Colore de acordo com a categoria alcgp
    # jitter=False = coloca todos os pontos em linha reta 
# Gráfico para mostrar a relação das variáveis categóricas com as continuas 
srn.catplot(x = 'alcgp', y = 'ncontrols', data = base5, col = 'tobgp')
    # Agrupa de acordo com o tobgp
    
    
    
# Gráficos 3D 
    
base6 = pd.read_csv('orchard.csv')
    # Temos 3 atributos numéricos e queremos plotar nas 3 dimensoes dele
from mpl_toolkits.mplot3d import axes3d

figura = plt.figure()
eixo = figura.add_subplot(1,1,1, projection='3d')
eixo.scatter(base6.decrease, base6.rowpos, base6.colpos)
eixo.set_xlabel('decrease')
eixo.set_ylabel('rowpos')
eixo.set_zlabel('colpos')

# Opções de cores:
# https://pythonspot.com/3d-scatterplot/