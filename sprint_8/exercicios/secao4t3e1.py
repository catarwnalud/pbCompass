"""
1. [Warm up]  Em Python, declare e inicialize uma lista contendo 250 inteiros obtidos de forma aleatória. 
Após, aplicar o método reverse sobre o conteúdo da lista e imprimir o resultado.

"""

import random

lista_inteiros = [random.randint(1, 1000) for _ in range(250)]

print("Lista original:")
print(lista_inteiros)

lista_inteiros.reverse()

print("\nLista invertida:")
print(lista_inteiros)
