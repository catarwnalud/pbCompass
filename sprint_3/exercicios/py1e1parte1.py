# Seção 3: Exercícios Python | - 1/2

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