import statistics
import pandas as pd
from statistics import mean

atores = pd.read_csv('actors.csv')

# ---------------------------------------------------------------------------------------------------------------------------------#

# 1.Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.

def max_num_filmes():

    ator_num_filme = atores[ atores['Number of Movies'] == max(atores['Number of Movies']) ]
    
    return  ator_num_filme [['Actor', 'Number of Movies']]

print('\n1. Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes:')
print(max_num_filmes())
print('#---------------------------------------------------------------------------------------------------------------------------------#')


# ---------------------------------------------------------------------------------------------------------------------------------#

# 2.Apresente a média da coluna contendo o número de filmes.

def media_filmes():


    media = statistics.mean(atores['Number of Movies'])
    return media

print('\n2. Apresente a média da coluna contendo o número de filmes: ', media_filmes())
print('#---------------------------------------------------------------------------------------------------------------------------------#')


# ---------------------------------------------------------------------------------------------------------------------------------#

# 3.Apresente o nome do ator/atriz com a maior média por filme.

def max_media_por_filme():

    maior_media = atores[ atores['Average per Movie'] == max(atores['Average per Movie']) ]

    return  maior_media[['Actor', 'Average per Movie']]

print('\n3. Apresente o nome do ator/atriz com a maior média por filme:')
print(max_media_por_filme())
print('#---------------------------------------------------------------------------------------------------------------------------------#')


# ---------------------------------------------------------------------------------------------------------------------------------#

# 4.Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

def filme_frequente():

    filme_mais_freq = atores['#1 Movie'].value_counts()

    return filme_mais_freq.head(1)


print('\n4. Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência:')
print(filme_frequente())
print('#---------------------------------------------------------------------------------------------------------------------------------#')

# ---------------------------------------------------------------------------------------------------------------------------------#