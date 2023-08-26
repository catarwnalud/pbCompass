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

"""
E2 - Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e
     o resultado deverá ser a contagem de vogais presentes em seu conteúdo.

     É obrigatório aplicar as seguintes funções:

     len

     filter

     lambda
"""

def conta_vogais(texto:str)-> int:
    vogais = 'aeiou'
    return len(list(filter(lambda t: t in vogais , texto.lower())))

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E4- A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos.
    Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %),
    as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos,
    a função deverá retornar o maior valor dentre eles.

    Veja o exemplo:

    Entrada

    operadores = ['+','-','*','/','+']
    operandos  = [(3,6), (-7, 4.9), (8,-8), (10,2), (8,4)]

    Aplicar as operações aos pares de operandos

    [ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 

    Obter o maior dos valores

    12

    Na resolução da atividade você deverá aplicar as seguintes funções:

    max

    zip

    map
"""


def op(tupla):

    if tupla[1] == '+':
        return tupla[0][0] + tupla[0][1]
    
    elif tupla[1] == '-':
        return tupla[0][0] - tupla[0][1]
    
    elif tupla[1] == '*':
        return tupla[0][0] * tupla[0][1]
    
    else:
        return tupla[0][0] / tupla[0][1]
    
    
def calcular_valor_maximo(operadores, operandos) -> float:

    resultado = list(map(op, zip(operandos, operadores)))

    return max(resultado)

operadores = ['+','-','*','/','+']
operandos  = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

print(calcular_valor_maximo(operadores, operandos))

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E5 - Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. 
     Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. 
     É o arquivo estudantes.csv de seu exercício.

     Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:

     Nome do estudante

     Três maiores notas, em ordem decrescente

     Média das três maiores notas, com duas casas decimais de precisão

     O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:

     Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>

     Exemplo:

     Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67

     Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33

     Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:

     round

     map

     sorted
"""
import csv

with open('estudantes.csv', 'r',  encoding = 'utf-8') as dados:

    diario = sorted(csv.reader(dados))

    nomes = []
    notas = []

    for linha in diario:
        linha[1:] = sorted(map(lambda x: int(x), linha[1:]), reverse = True)
        notas.append(linha[1:4])
        nomes.append(linha[0])
    
    medias = list(map(lambda  l: (l[0]+l[1]+ l[2])/ len(l), notas))

for i in range(len(medias)):
    print('Nome: {} Notas: {} Média: {}'.format(nomes[i], notas[i], round(medias[i],2)))

#--------------------------------------------------------------------------------------------------------------------------------------#