#--------------------------------------------------------------------------------------------------------------------------------------#
# Seção 3: Exercícios Python | - 1/2
#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E1 - Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa.
     Como saída, imprima o ano em que a pessoa completará 100 anos de idade.
"""

from datetime import datetime

nome = input('Seu nome: ')
idade = int(input('Sua idade: '))

data_atual = datetime.now()

anos_nasc = data_atual.year - idade

ano_cem = anos_nasc + 100

print (ano_cem)

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E2 - Escreva um código Python para verificar se três números digitados na entrada padrão são pares ou ímpares. 
     Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).

     Importante: Aplique a função range() em seu código.
"""

for i in range (0,3):
    num = int(input())

    if num % 2 == 0:
        print("Par: {}".format(num))
    else:
        print("Ímpar: {}".format(num))

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E3 - Escreva um código Python para imprimir os números pares de 0 até 20 (incluso).

     Importante: Aplique a função range() em seu código.
"""

for i in range(0,21):
    if i % 2 == 0:
        print('{}'.format(i))

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E4 - Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
     Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.

     Importante: Aplique a função range().
"""

for i in range(2, 101): 
        for j in range(2,i): 
            if i % j == 0: 
                break
        else: 
            print("{}".format(i)) 

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
E5 - Escreva um código Python que declara 3 variáveis:
     dia, inicializada com valor 22
     mes, inicializada com valor 10 e
     ano, inicializada com valor 2022
    
     Como saída, você deverá imprimir a data correspondente, no formato a seguir dia/mes/ano.
"""

dia = 22
mes = 10
ano = 2022

print("{}/{}/{}".format(dia, mes, ano))

#--------------------------------------------------------------------------------------------------------------------------------------#