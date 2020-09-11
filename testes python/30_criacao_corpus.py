# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 21:23:06 2020

@author: Giovanni
"""

# Criação de Corpus com Python 

import matplotlib.pyplot as plt 
import nltk # Já vem no anaconda 

# nltk.download() 
    # abre uma janela de download de todos os pacotes adicionais 

# Criando o Corpus: 
from nltk.corpus import PlaintextCorpusReader 

corpus = PlaintextCorpusReader('Dados', '.*') # .* = todas as extensões 

arquivos = corpus.fileids() # Cria uma lista com todos os arquivos da pasta 

# Observando os arquivos: 
arquivos[0]
arquivos[0:100]
for a in arquivos:
    print(a)
    
# Vendo o texto de um arquivo: 
texto = corpus.raw('1.txt')

# Acessar o texto de todo o corpus: 
todo_texto = corpus.raw()

# Acessar cada uma das palavras que existem no corpus: 
palavras = corpus.words()

len(palavras)
# Out[8]: 244913
# esse é o número de palavras do arquivo 

# Geração da Nuvem de Palavras 
from nltk.corpus import stopwords 
from matplotlib.colors import ListedColormap 
from wordcloud import WordCloud # Biblioteca para trabalhar com nuvem de palavras 
# pip install wordcloud

# Verificando a lista das stopwords: 
stopwords.words('portuguese')

stops = stopwords.words('english')

# Mapa Cores = cores que iremos preencher nossa lista de palavras 
mapa_cores = ListedColormap(['orange', 'green', 'red', 'magenta'])

# Criando a nuvem de palavras: 
nuvem = WordCloud(background_color='white', colormap=mapa_cores, stopwords=stops, max_words=100)

# Gerando a nuvem: 
nuvem.generate(todo_texto)

plt.imshow(nuvem)

# Matriz de Termos Frequentes: 

# Primeiro vamos remover as stopwords 
palavras_semstop = [p for p in palavras if p not in stops]
len(palavras_semstop)
# Removendo pontuação: 
import string 

palavras_sem_pontuacao = [p for p in palavras_semstop if p not in string.punctuation]

frequencia = nltk.FreqDist(palavras_sem_pontuacao)

mais_comuns = frequencia.most_common(100)