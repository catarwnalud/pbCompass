#--------------------------------------------------------------------------------------------------------------------------------------#
# Seção 2: Exercícios 
#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E1 - Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions,
     apresente os 5 maiores valores pares e a soma destes.

     Você deverá aplicar as seguintes funções no exercício:

     map

     filter

     sorted

     sum

     Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):

     a lista dos 5 maiores números pares em ordem decrescente;
     a soma destes valores.
"""

with open('number.txt') as dados:

    lista = []
    
    for linha in dados.readlines():
        map(lista.append(int(linha)), dados)


def ordenaDesc(lista):
    lista_ord = sorted(lista, reverse = True )
    return pares(lista_ord)


def pares(lista):
    return list(filter(lambda p: p % 2 == 0, lista))


def pares_soma(lista):
    lista_pares = ordenaDesc(lista)
    print(lista_pares[0:5])
    return sum(lista_pares[0:5])

print(pares_soma(lista))

#--------------------------------------------------------------------------------------------------------------------------------------#