"""
2. Em Python, declare e inicialize uma lista contendo o nome de 20 animais. Ordene-os em ordem crescente e itere sobre os itens, 
imprimindo um a um (você pode utilizar list comprehension aqui). Na sequência, armazene o conteúdo da lista em um arquivo de texto,
 um item em cada linha, no formato CSV.

"""

animais = [
    "Cachorro", "Gato", "Leão", "Elefante", "Girafa", "Tigre", "Urso", "Rato",
    "Panda", "Cobra", "Cavalo", "Coelho", "Pássaro", "Peixe", "Macaco", "Porco",
    "Coruja", "Raposa", "Baleia", "Foca"
]

animais_ordenados = sorted(animais)

print("Animais em ordem crescente:")
[print(animal) for animal in animais_ordenados]

with open("animais.csv", "w") as file:
    for animal in animais_ordenados:
        file.write(f"{animal}\n")
