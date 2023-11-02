"""
1. Inicialmente iremos preparar o ambiente, definindo o diretório onde nosso código será desenvolvido. 
Para este diretório iremos copiar o arquivo nomes_aleatorios.txt.

Após, em nosso script Python, devemos importar as bibliotecas necessárias:

from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

Aplicando as bibliotecas do Spark, podemos definir a Spark Session e sobre ela definir o Context para habilitar o módulo SQL

spark = SparkSession \
                .builder \
                .master("local[*]")\
                .appName("Exercicio Intro") \
                .getOrCreate()

Nesta etapa, adicione código para ler o arquivo nomes_aleatorios.txt através do comando spark.read.csv. 
Carregue-o para dentro de um dataframe chamado df_nomes e, por fim, liste algumas linhas através do método show. Exemplo: df_nomes.show(5)

"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes.show(5)

"""
2. No Python, é possível acessar uma coluna de um objeto dataframe pelo atributo (por exemplo df_nomes.nome) ou por índice (df_nomes['nome']).
Enquanto a primeira forma é conveniente para a exploração de dados interativos, você deve usar o formato de índice, pois caso algum nome 
de coluna não esteja de acordo seu código irá falhar.

Como não informamos no momento da leitura do arquivo, o Spark não identificou o Schema por padrão e definiu todas as colunas como string.
Para ver o Schema, use o método df_nomes.printSchema().

Nesta etapa, será necessário adicionar código para renomear a coluna para Nomes, imprimir o esquema e mostrar 10 linhas do dataframe.

"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

df_nomes.printSchema()

df_nomes.show(10)

"""
3. Ao dataframe (df_nomes), adicione nova coluna chamada Escolaridade e atribua para cada linha um dos três valores de forma aleatória:
Fundamental, Medio ou Superior.

"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
import random


spark = SparkSession.builder.appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

df_nomes = df_nomes.withColumn('Escolaridade', when((random.randint(1, 3) == 1), "Fundamental")
                                     .when((random.randint(1, 3) == 2), "Médio")
                                     .otherwise("Superior"))
df_nomes.show(10)


"""
4. Ao dataframe (df_nomes), adicione nova coluna chamada Pais e atribua para cada linha o nome de um dos 
13 países da América do Sul, de forma aleatória.
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import random


spark = SparkSession.builder.appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

df_nomes = df_nomes.withColumn('Escolaridade', when((random.randint(1, 3) == 1), "Fundamental")
                                     .when((random.randint(1, 3) == 2), "Médio")
                                     .otherwise("Superior"))

paises_america_sul = ["Brasil", "Argentina", "Colômbia", "Peru", "Venezuela", "Chile", 
                      "Equador", "Bolívia", "Paraguai", "Uruguai", "Guiana", "Suriname", "Guiana Francesa"]

df_nomes = df_nomes.withColumn('Pais', col("Nomes"))  

for row in df_nomes.rdd.collect():
    df_nomes = df_nomes.withColumn('Pais', 
                                   when(col('Nomes') == row['Nomes'], 
                                        paises_america_sul[random.randint(0, len(paises_america_sul) - 1)]).otherwise(col('Pais')))
df_nomes.show(10)

"""
5. Ao dataframe (df_nomes), adicione nova coluna chamada AnoNascimento e atribua para cada linha um valor de ano entre 1945 e 2010, 
de forma aleatória. 

"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import random


spark = SparkSession.builder.appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

df_nomes = df_nomes.withColumn('Escolaridade', when((random.randint(1, 3) == 1), "Fundamental")
                                     .when((random.randint(1, 3) == 2), "Médio")
                                     .otherwise("Superior"))

paises_america_sul = ["Brasil", "Argentina", "Colômbia", "Peru", "Venezuela", "Chile", 
                      "Equador", "Bolívia", "Paraguai", "Uruguai", "Guiana", "Suriname", "Guiana Francesa"]

df_nomes = df_nomes.withColumn('Pais', col("Nomes"))  

for row in df_nomes.rdd.collect():
    df_nomes = df_nomes.withColumn('Pais', 
                                   when(col('Nomes') == row['Nomes'], 
                                        paises_america_sul[random.randint(0, len(paises_america_sul) - 1)]).otherwise(col('Pais')))
    
df_nomes = df_nomes.withColumn('AnoNascimento', (1945 + (random.randint(0, 65))))


"""
6. Usando o método select do dataframe (df_nomes), 
selecione as pessoas que nasceram neste século. Armazene o resultado em outro dataframe chamado df_select e mostre 10 nomes deste

"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import random


spark = SparkSession.builder.appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

df_nomes = df_nomes.withColumn('Escolaridade', when((random.randint(1, 3) == 1), "Fundamental")
                                     .when((random.randint(1, 3) == 2), "Médio")
                                     .otherwise("Superior"))

paises_america_sul = ["Brasil", "Argentina", "Colômbia", "Peru", "Venezuela", "Chile", 
                      "Equador", "Bolívia", "Paraguai", "Uruguai", "Guiana", "Suriname", "Guiana Francesa"]

df_nomes = df_nomes.withColumn('Pais', col("Nomes"))  

for row in df_nomes.rdd.collect():
    df_nomes = df_nomes.withColumn('Pais', 
                                   when(col('Nomes') == row['Nomes'], 
                                        paises_america_sul[random.randint(0, len(paises_america_sul) - 1)]).otherwise(col('Pais')))
    
df_nomes = df_nomes.withColumn('AnoNascimento', (1945 + (random.randint(0, 65))))

df_select = df_nomes.select("Nomes", "AnoNascimento").filter((col("AnoNascimento") >= 2001) & (col("AnoNascimento") <= 2023))

df_select.show(10)

"""
7. Usando Spark SQL repita o processo da Pergunta 6. Lembre-se que, para trabalharmos com SparkSQL, 
precisamos registrar uma tabela temporária e depois executar o comando SQL. 
Abaixo um exemplo de como executar comandos SQL com SparkSQL:

df_nomes.createOrReplaceTempView ("pessoas")

spark.sql("select * from pessoas").show()
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import random


spark = SparkSession.builder.appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

df_nomes = df_nomes.withColumn('Escolaridade', when((random.randint(1, 3) == 1), "Fundamental")
                                     .when((random.randint(1, 3) == 2), "Médio")
                                     .otherwise("Superior"))

paises_america_sul = ["Brasil", "Argentina", "Colômbia", "Peru", "Venezuela", "Chile", 
                      "Equador", "Bolívia", "Paraguai", "Uruguai", "Guiana", "Suriname", "Guiana Francesa"]

df_nomes = df_nomes.withColumn('Pais', col("Nomes"))  

for row in df_nomes.rdd.collect():
    df_nomes = df_nomes.withColumn('Pais', 
                                   when(col('Nomes') == row['Nomes'], 
                                        paises_america_sul[random.randint(0, len(paises_america_sul) - 1)]).otherwise(col('Pais')))
    
df_nomes = df_nomes.withColumn('AnoNascimento', (1945 + (random.randint(0, 65))))

df_nomes.createOrReplaceTempView("pessoas")

query = """
    SELECT Nomes
    FROM pessoas
    WHERE AnoNascimento >= 2001
    LIMIT 10
"""

df_select = spark.sql(query)

df_select.show()

"""
8. Usando o método select do Dataframe df_nomes, 
Conte o número de pessoas que são da geração Millennials (nascidos entre 1980 e 1994) no Dataset

"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import random


spark = SparkSession.builder.appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

df_nomes = df_nomes.withColumn('Escolaridade', when((random.randint(1, 3) == 1), "Fundamental")
                                     .when((random.randint(1, 3) == 2), "Médio")
                                     .otherwise("Superior"))

paises_america_sul = ["Brasil", "Argentina", "Colômbia", "Peru", "Venezuela", "Chile", 
                      "Equador", "Bolívia", "Paraguai", "Uruguai", "Guiana", "Suriname", "Guiana Francesa"]

df_nomes = df_nomes.withColumn('Pais', col("Nomes"))  

for row in df_nomes.rdd.collect():
    df_nomes = df_nomes.withColumn('Pais', 
                                   when(col('Nomes') == row['Nomes'], 
                                        paises_america_sul[random.randint(0, len(paises_america_sul) - 1)]).otherwise(col('Pais')))
    
df_nomes = df_nomes.withColumn('AnoNascimento', (1945 + (random.randint(0, 65))))

count_millennials = df_nomes.select("Nomes").filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994)).count()

print(f"O número de pessoas da geração Millennials é: {count_millennials}")

"""
9. Repita o processo da Pergunta 8 utilizando Spark SQL

"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import random


spark = SparkSession.builder.appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

df_nomes = df_nomes.withColumn('Escolaridade', when((random.randint(1, 3) == 1), "Fundamental")
                                     .when((random.randint(1, 3) == 2), "Médio")
                                     .otherwise("Superior"))

paises_america_sul = ["Brasil", "Argentina", "Colômbia", "Peru", "Venezuela", "Chile", 
                      "Equador", "Bolívia", "Paraguai", "Uruguai", "Guiana", "Suriname", "Guiana Francesa"]

df_nomes = df_nomes.withColumn('Pais', col("Nomes"))  

for row in df_nomes.rdd.collect():
    df_nomes = df_nomes.withColumn('Pais', 
                                   when(col('Nomes') == row['Nomes'], 
                                        paises_america_sul[random.randint(0, len(paises_america_sul) - 1)]).otherwise(col('Pais')))
    
df_nomes = df_nomes.withColumn('AnoNascimento', (1945 + (random.randint(0, 65))))

df_nomes.createOrReplaceTempView("pessoas")

query = """
    SELECT COUNT(*) AS Total_Millennials
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1980 AND 1994
"""

df_millennials = spark.sql(query)

df_millennials.show()

"""
10. Usando Spark SQL, obtenha a quantidade de pessoas de cada país para uma das gerações abaixo.
 Armazene o resultado em um novo dataframe e depois mostre todas as linhas em ordem crescente de Pais, Geração e Quantidade

- Baby Boomers - nascidos entre 1944 e 1964;

- Geração X - nascidos entre 1965 e 1979;4

- Millennials (Geração Y) - nascidos entre 1980 e 1994;

- Geração Z - nascidos entre 1995 e 2015.

"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import random


spark = SparkSession.builder.appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes = df_nomes.withColumnRenamed('_c0', 'Nomes')

df_nomes = df_nomes.withColumn('Escolaridade', when((random.randint(1, 3) == 1), "Fundamental")
                                     .when((random.randint(1, 3) == 2), "Médio")
                                     .otherwise("Superior"))

paises_america_sul = ["Brasil", "Argentina", "Colômbia", "Peru", "Venezuela", "Chile", 
                      "Equador", "Bolívia", "Paraguai", "Uruguai", "Guiana", "Suriname", "Guiana Francesa"]

df_nomes = df_nomes.withColumn('Pais', col("Nomes"))  

for row in df_nomes.rdd.collect():
    df_nomes = df_nomes.withColumn('Pais', 
                                   when(col('Nomes') == row['Nomes'], 
                                        paises_america_sul[random.randint(0, len(paises_america_sul) - 1)]).otherwise(col('Pais')))
    
df_nomes = df_nomes.withColumn('AnoNascimento', (1945 + (random.randint(0, 65))))

df_nomes.createOrReplaceTempView("pessoas")

query = """
    SELECT Pais, 
           CASE 
               WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
               WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
               WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
               WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
               ELSE 'Outros' 
           END AS Geração, 
           COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Pais, Geração
    ORDER BY Pais, Geração, Quantidade
"""

df_resultado = spark.sql(query)

df_resultado.show()
