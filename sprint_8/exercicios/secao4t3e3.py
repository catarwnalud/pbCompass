"""
3. Elaborar um código Python para gerar um dataset de nomes de pessoas.

"""

import random
import time
import os
import names

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []
for i in range(qtd_nomes_unicos):
    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))
dados = [random.choice(aux) for i in range(qtd_nomes_aleatorios)]

nome_arquivo = "nomes_aleatorios.txt"
with open(nome_arquivo, "w") as file:
    for nome in dados:
        file.write(f"{nome}\n")
