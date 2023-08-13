#--------------------------------------------------------------------------------------------------------------------------------------#
# Seção 4: Exercícios Python | - 2/2
#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E6 - Considere as duas listas abaixo:

     a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
     b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
     
     Escreva um programa para avaliar o que ambas as listas têm em comum (sem repetições),
     imprimindo a lista de valores da interseção na saída padrão.
"""

a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

inter = []

for i in a:
    if i in b:
        inter.append(i)

inter_set = list(set(inter))

print(inter_set)

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E7 - Dada a seguinte lista:
     
     a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
     
     Faça um programa que gere uma nova lista contendo apenas números ímpares.
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

impares = []

for i in range(len(a)):
    if a[i] % 2 != 0:
        impares.append(a[i])

print(impares)

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E8 - Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.
     
     Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
     
     É necessário que você imprima no console exatamente assim:
     
     A palavra: maça não é um palíndromo
     A palavra: arara é um palíndromo
     A palavra: audio não é um palíndromo
     A palavra: radio não é um palíndromo
     A palavra: radar é um palíndromo
     A palavra: moto não é um palíndromo
"""

lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in range(len(lista)):
     if lista[i] == lista[i][::-1]:
          print("A palavra: {} é um palíndromo".format(lista[i]))
     else:
          print("A palavra: {} não é um palíndromo".format(lista[i]))

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E9 - Dada as listas a seguir:

     primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
     sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
     idades = [19, 28, 25, 31]
     
     Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".
     
     Exemplo:
     0 - João Soares está com 19 anos
"""

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
     
for i, nome in enumerate(primeirosNomes):
    print("{} - ".format(i), end = '')
    print("{} ".format(nome), end = '')
    print("{} ".format(sobreNomes[i]), end = '')
    print("está com {} anos".format(idades[i]))

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E10 - Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. 
      Utilize a lista a seguir para testar sua função.

      ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
"""

def semD(lista_p):
      
      lista_p = list(set(lista_p))
      
      return lista_p
    
l = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
print("{}".format(semD(l)))

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E11 - Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
      Dica: leia a documentação da função open(...)
"""
file = open("arquivo_texto.txt", "r")
print("{}".format(file.read()),end = '')

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E12 - Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
      Dica: leia a documentação do pacote json
"""

import json

file_j = open("person.json",'r')
file_p = json.loads(file_j.read())

print(file_p)

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E13 - Implemente a função my_map(f, list) que recebe uma lista como primeiro argumento e uma função como segundo argumento.
      Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.
      
      Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def my_map (val):
    return pow(val,2)

print("{}".format(list(map(my_map,lista))))

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E14 - Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados 
      e imprime o valor de cada parâmetro recebido.
      
      Teste sua função com os seguintes parâmetros:
      
      (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
"""

def func (*parm, **args):

      for i in parm:
            print(i)

      for i in args.values():
            print (i)
            
      return 0

func(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

#--------------------------------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E16 - Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles.
      Depois imprima a soma dos valores.
      
      A string deve ter valor  "1,3,4,6,10,76"
"""

def soma (string):

    soma = 0
    for i in range(len(string)):
        soma += int(string[i])

    return soma

teste = "1,3,4,6,10,76"

string = teste.split(',')

print("{}".format(soma(string)))

#--------------------------------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E18 - Dado o dicionário a seguir:
      speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
      
      Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.
"""

speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

lista = []

for i in speed.values():
    lista.append(i)

lista = list(set(lista))

print(lista)

#--------------------------------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E20 - Imprima a lista abaixo de trás para frente.
      a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(a[::-1])

#--------------------------------------------------------------------------------------------------------------------------------------#