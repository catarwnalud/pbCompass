#--------------------------------------------------------------------------------------------------------------------------------------#
# Seção 7: Exercícios Python || - 2/2
#--------------------------------------------------------------------------------------------------------------------------------------#

# Extração, Transformação e Carregamento

"""
0.1. Extração 
"""
with open ('actors.csv') as dados:

    lista = []
    arquivo = dados.readlines()

    for linha, conteudo in enumerate(arquivo):
         lista.append((arquivo[linha].strip().rsplit(',', 5)))

    lista = lista[1:]

    for linha in lista:
        for indice, conteudo in enumerate(linha):
            if indice == 1 or indice == 2 or indice == 3 or indice == 5:
                linha[indice] = float(linha[indice])

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
1. Apresente o ator/atriz com maior número de filmes e a respectiva quantidade.
"""

def quantidade_filmes():

    quant_filmes = 0
    for linha in lista:
        if quant_filmes < linha[2]:
            quant_filmes = int(linha[2])
            artista = linha[0]

    return artista, quant_filmes

# Carregamento

with open ('etapa1.txt', 'w') as resposta:
        resposta.write('Ator/Atriz com mais filmes: %s, quantidade de filmes: %d\n' % quantidade_filmes())

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
2. Apresente a  média de faturamento bruto por ator.
"""

def faturamento_medio():
    
    artistas = []
    f_medio = []
    for linha in lista:
        artistas.append(linha[0])
        f_medio.append(linha[3])
    
    return artistas, f_medio

artistas, f_medio = faturamento_medio()

# Carregamento

with open ('etapa2.txt', 'w', encoding = 'utf-8') as resposta:
        for i in range(len(artistas)):
            resposta.write('Ator/Atriz: %s, faturamento: %.2f \n' % (artistas[i], f_medio[i]))
    
#--------------------------------------------------------------------------------------------------------------------------------------#

"""
3. Apresente o ator/atriz com a maior média de faturamento por filme.
"""

def maior_faturamento():
     
    ftm = 0
    for linha in lista:
        if ftm < linha[3]:
            artista = linha[0]

    return artista

# Carregamento

with open ('etapa3.txt', 'w') as resposta:
        resposta.write('Ator/Atriz com maior faturamento: %s\n' % maior_faturamento())

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
4. O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
"""

def filmes():

    filme = []
    for linha in lista:
        filme.append(linha[4])

    f_semR = sorted(list(set(filme)))
    quantidade = []

    for f in f_semR:
        quant = filme.count(f)
        quantidade.append(quant)

    maior_quant = max(quantidade)
    f_fnqt = ''

    for i in range (len(f_semR)):
        if quantidade[i] == maior_quant:
            f_fnqt = f_semR[i]
        
    return f_fnqt, maior_quant

# Carregamento

with open ('etapa4.txt', 'w', encoding = 'utf-8') as resposta:
        resposta.write("Nome do filme mais frequente: %s, frequência: %d" % filmes())

#--------------------------------------------------------------------------------------------------------------------------------------#

"""
5. A lista dos atores ordenada pelo faturamento bruto total, em ordem decrescente.
"""

def ordem_ftm():

    bruto_total = []
    artista = []

    for linha in lista:
        artista.append(linha[0])
        bruto_total.append(linha[1])

    return artista,bruto_total

ator, ftm = ordem_ftm()

# Carregamento

with open ('etapa5.txt', 'w', encoding = 'utf-8') as resposta:
        for i in range(len(ator)):
            resposta.write('Ator/Atriz: %s, faturamento bruto total: %.2f \n' % (ator[i],ftm[i]))
    
#--------------------------------------------------------------------------------------------------------------------------------------#