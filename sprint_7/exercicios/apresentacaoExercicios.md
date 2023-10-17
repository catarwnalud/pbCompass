#
# Exercícios da Sprint 7

###  Seção 3: Exercícios

- Tarefa 1: Python com Pandas e Numpy

    - [Código](secao3e1.py)

        - [Resultado](atores.png)

#

- Tarefa 2: Apache Spark - Contador de Palavras

     - [Código](pyspark_contador.png)

        - [Resultado](contagem.txt)

#

###  Seção 4: Labolatório AWS

- Ler o arquivo nomes.csv no S3 (lembre-se de realizar upload do arquivo antes) 

    - [Código](labglue1.py)

        - [Resultado](labglue1.png)

#

- Imprima o schema do dataframe gerado no passo anterior

    - [Código](labglue2.py)

        - [Resultado](labglue2.png)

#

- Escrever o código necessário para alterar a caixa dos valores da coluna nome para MAIÚSCULO

    - [Código](labglue3.py)

        - [Resultado](labglue3.png)

#

- Imprimir a contagem de linhas presentes no dataframe

    - [Código](labglue4.py)

        - [Resultado](labglue4.png)

#

- Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo. Ordene os dados de modo que o ano mais recente apareça como primeiro registro do dataframe.

    - [Código](labglue5.py)

        - [Resultado](labglue5.png)

#

- Apresentar qual foi o nome feminino com mais registros e em que ano ocorreu 

    - [Código](labglue6.py)

        - [Resultado](labglue6.png)

#

- Apresentar qual foi o nome masculino com mais registros e em que ano ocorreu 

    - [Código](labglue7.py)

        - [Resultado](labglue7.png)

#

- Apresentar o total de registros (masculinos e femininos) para cada ano presente no dataframe. Considere apenas as primeiras 10 linhas, ordenadas pelo ano, de forma crescente

    - [Código](labglue8.py)

        - [Resultado](labglue8.png)

#

- Escrever o conteúdo do dataframe com os valores de nome em maiúsculo no S3. Atenção aos requisitos:
		
	- A gravação deve ocorrer no subdiretório frequencia_registro_nomes_eua do path s3://<BUCKET>/lab-glue/
	- O formato deve ser JSON
	- O particionamento deverá ser realizado pelas colunas sexo e ano (nesta ordem) 

    - [Código](labglue9.py)

        - [Resultado](labglue9.json)

#

###  Seção 5: Desafio - Parte | 

-  1) Implementar código Python:

    - ler os 2 arquivos (filmes e series) no formato CSV inteiros, ou seja, sem filtrar os dados

    - utilizar a lib boto3 para carregar os dados para a AWS

    - acessar a AWS e grava no S3, no bucket definido com RAW Zone

        - no momento da gravação dos dados deve-se considerar o padrão: <nome do bucket>\<camada de armazenamento>\<origem do dado>\<formato do dado>\<especificação do dado>\<data de processamento separada por ano\mes\dia>\<arquivo>

                Por exemplo:

                    S3:\\data-lake-do-fulano\Raw\Local\CSV\Movies\2022\05\02\movies.csv

                    S3:\\data-lake-do-fulano\Raw\Local\CSV\Series\2022\05\02\series.csv

    2) Criar container Docker com um volume para armazenar os arquivos CSV e executar processo Python implementado

    3) Executar localmente o container docker para realizar a carga dos dados ao S3

    - [Código .py](img.py)

    - [Dockerfile](dockerfile)

#
