# MOVIES.CSV:

# Os dados dos arquivo_*.json (antigo movies.csv) da camada Raw estão sendo tradados e enviados para a Trusted

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import when, col, coalesce, avg, floor

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

source_file = "s3://dados-desafio/Raw/Local/JSON/Movies/2023/10/27/arquivo_*.json" # Local do arquivo_*.json
target_path = "s3://dados-desafio/Trusted/Movies/" # Destino dos dados tratados

data_frame = spark.read.json(source_file) 

data_frame = data_frame.withColumnRenamed("tituloPincipal", "tituloPrincipal") # Trata erro do nome da coluna

media_tempo_minutos = round(data_frame.select(avg("tempoMinutos")).collect()[0][0], 1 ) # Faz a média da coluna tempoMinutos

data_frame = data_frame.withColumn("tempoMinutos", when(col("tempoMinutos") == 'NULL', media_tempo_minutos).otherwise(col("tempoMinutos"))) # Substitui os nulos de tempoMinutos pela média de tempoMinutos

data_frame_atualizado = data_frame.withColumn("tempoHoras", when(col("tempoMinutos") < 60, 1).otherwise(col("tempoMinutos") / 60)) # Coluna com o tempo em horas

# Faz uma coluna de classificação de horas dos filmes
data_frame_atualizado = data_frame_atualizado.withColumn(
    "classificacao_horas_numerica",
    when(col("tempoHoras") < 1, 0)
    .when((col("tempoHoras") >= 1) & (col("tempoHoras") <= 1.5), 1)
    .when((col("tempoHoras") > 1.5) & (col("tempoHoras") <= 2.5), 2)
    .when((col("tempoHoras") > 2.5) & (col("tempoHoras") <= 3.5), 3)
    .otherwise(4)
)

# Faz uma coluna de classificação de horas dos filmes
data_frame_atualizado = data_frame_atualizado.withColumn(
    "classificacao_horas_escrita",
    when(col("tempoHoras") < 1, "Menos de uma hora")
    .when((col("tempoHoras") >= 1) & (col("tempoHoras") <= 1.5), "Uma hora a uma hora e meia")
    .when((col("tempoHoras") > 1.5) & (col("tempoHoras") <= 2.5), "Duas horas a duas horas e meia")
    .when((col("tempoHoras") > 2.5) & (col("tempoHoras") <= 3.5), "Três horas a três horas e meia")
    .otherwise("Mais de três horas e meia")
)

# Faz uma coluna de classificação do ano de lançamento em intervalos de 5 anos
data_frame_atualizado = data_frame_atualizado.withColumn(
    "classificacao_ano",
    floor(col("anoLancamento") / 5) * 5
)

# Faz uma coluna de classificação da nota média dos filmes
data_frame_atualizado = data_frame_atualizado.withColumn(
    "classificacao_nota_numerica",
    when((col("notaMedia") > 0) & (col("notaMedia") < 1), 1)
    .when((col("notaMedia") >= 1) & (col("notaMedia") < 2), 2)
    .when((col("notaMedia") >= 2) & (col("notaMedia") < 3), 3)
    .when((col("notaMedia") >= 3) & (col("notaMedia") < 4), 4)
    .when((col("notaMedia") >= 4) & (col("notaMedia") < 5), 5)
    .when((col("notaMedia") >= 5) & (col("notaMedia") < 6), 6)
    .when((col("notaMedia") >= 6) & (col("notaMedia") < 7), 7)
    .when((col("notaMedia") >= 7) & (col("notaMedia") < 8), 8)
    .when((col("notaMedia") >= 8) & (col("notaMedia") < 9), 9)
    .when((col("notaMedia") >= 9) & (col("notaMedia") <= 10), 10)
    .otherwise(0)  
)

# Faz uma coluna de classificação da nota média dos filmes
data_frame_atualizado = data_frame_atualizado.withColumn(
    "classificacao_nota_escrita",
    when((col("notaMedia") >= 1) & (col("notaMedia") < 2), "1 a menos de 2")
    .when((col("notaMedia") >= 2) & (col("notaMedia") < 3), "2 a menos de 3")
    .when((col("notaMedia") >= 3) & (col("notaMedia") < 4), "3 a menos de 4")
    .when((col("notaMedia") >= 4) & (col("notaMedia") < 5), "4 a menos de 5")
    .when((col("notaMedia") >= 5) & (col("notaMedia") < 6), "5 a menos de 6")
    .when((col("notaMedia") >= 6) & (col("notaMedia") < 7), "6 a menos de 7")
    .when((col("notaMedia") >= 7) & (col("notaMedia") < 8), "7 a menos de 8")
    .when((col("notaMedia") >= 8) & (col("notaMedia") < 9), "8 a menos de 9")
    .when((col("notaMedia") >= 9) & (col("notaMedia") <= 10), "9 a 10")
    .otherwise("Sem nota")  
)

# Faz uma coluna de classificação do numero de votos 
data_frame_atualizado = data_frame_atualizado.withColumn(
    "classificacao__votos_escrita",
    when((col("numeroVotos") >= 1) & (col("numeroVotos") <= 50), "1 - 50 votos")
    .when((col("numeroVotos") > 50) & (col("numeroVotos") <= 100), "51 - 100 votos")
    .when((col("numeroVotos") > 100) & (col("numeroVotos") <= 500), "101 - 500 votos")
    .when((col("numeroVotos") > 500) & (col("numeroVotos") <= 1000), "501 - 1000 votos")
    .when((col("numeroVotos") > 1000) & (col("numeroVotos") <= 2000), "1001 - 2000 votos")
    .when((col("numeroVotos") > 2000) & (col("numeroVotos") <= 3000), "2001 - 3000 votos")
    .when((col("numeroVotos") > 3000) & (col("numeroVotos") <= 5000), "3001 - 5000 votos")
    .when(col("numeroVotos") > 5000, "Mais de 5000 votos")
    .otherwise("Sem votos")
)

colunas_ordenadas = ["id", "tituloPrincipal", "tituloOriginal", "anoLancamento",  "classificacao_ano", "tempoMinutos", "tempoHoras", "classificacao_horas_numerica", "classificacao_horas_escrita", "genero", "notaMedia",  "classificacao_nota_escrita",   "classificacao_nota_numerica", "numeroVotos", "classificacao__votos_escrita", "generoArtista", "personagem", "nomeArtista", "anoNascimento",  "anoFalecimento", "profissao", "titulosMaisConhecidos"] 

                       
data_frame_atualizado = data_frame_atualizado.select(colunas_ordenadas)

for column in data_frame_atualizado.columns: # Corrige outros valores nulos
    data_frame_atualizado = data_frame_atualizado.withColumn(column, when(col(column) == "\\N", None).otherwise(col(column)))
    data_frame_atualizado = data_frame_atualizado.withColumn(column, when(col(column) == "null", None).otherwise(col(column)))

dynamic_frame = DynamicFrame.fromDF(data_frame_atualizado, glueContext, "dynamic_frame_name")

glueContext.write_dynamic_frame.from_options( # Envia os dados para o destino
    frame = dynamic_frame,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "parquet"
    )     
   
job.commit()

# SERIES.CSV:

# Os dados dos arquivo_*.json (antigo series.csv) da camada Raw estão sendo tradados e enviados para a Trusted

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import when, col

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

source_file = "s3://dados-desafio/Raw/Local/JSON/Series/2023/10/27/arquivo_*.json" # Local do arquivo_*.json
target_path = "s3://dados-desafio/Trusted/Series/" # Destino dos dados tratados

data_frame = spark.read.json(source_file)

colunas_ordenadas = ["id", "tituloPincipal", "tituloOriginal", "anoLancamento", "tempoMinutos", 
                     "genero", "notaMedia", "numeroVotos", "generoArtista", "personagem", "nomeArtista", "anoNascimento", 
                       "anoFalecimento", "profissao", "titulosMaisConhecidos"]

data_frame = data_frame.select(colunas_ordenadas) # Ordena as colunas

data_frame = data_frame.withColumnRenamed("tituloPincipal", "tituloPrincipal") # Trata erro do nome da coluna

for column in data_frame.columns: # Trata os dados nulos
   data_frame = data_frame.withColumn(column, when(col(column) == "\\N", "NULL").otherwise(col(column)))
   
dynamic_frame = DynamicFrame.fromDF(data_frame, glueContext, "dynamic_frame_name")

glueContext.write_dynamic_frame.from_options( # Envia os dados no formato parquet para o destino
    frame = dynamic_frame,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "parquet"
    )     
      
job.commit()

# MOVIES DO TMDB

# Os dados dos arquivo_*.json (provindo da chamada a api do TMDB) da camada Raw estão sendo tradados e enviados para a Trusted

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import when, col, coalesce, avg, floor, format_number

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

source_file = "s3://dados-desafio/Raw/TMDB/JSON/Movies/2023/10/27/arquivo_*.json" # Local do arquivo_*.json
target_path = "s3://dados-desafio/Trusted/TMDB/Movies/2023/10/27/" # Destino dos dados tratados

data_frame = spark.read.json(source_file) 

media_tempo_minutos = round(data_frame.select(avg("tempoMinutos")).collect()[0][0], 1 ) # Faz a média da coluna tempoMinutos

data_frame = data_frame.withColumn("tempoMinutos", when(col("tempoMinutos") == 'NULL', media_tempo_minutos).otherwise(col("tempoMinutos"))) # Substitui os nulos de tempoMinutos pela média de tempoMinutos

data_frame_atualizado = data_frame.withColumn("tempoHoras", when(col("tempoMinutos") < 60, 1).otherwise(col("tempoMinutos") / 60)) # Coluna com o tempo em horas

# Faz uma coluna de classificação de horas dos filmes
data_frame_atualizado = data_frame_atualizado.withColumn(
    "classificacao_horas_numerica",
    when(col("tempoHoras") < 1, 0)
    .when((col("tempoHoras") >= 1) & (col("tempoHoras") <= 1.5), 1)
    .when((col("tempoHoras") > 1.5) & (col("tempoHoras") <= 2.5), 2)
    .when((col("tempoHoras") > 2.5) & (col("tempoHoras") <= 3.5), 3)
    .otherwise(4)
)

# Faz uma coluna de classificação de horas dos filmes
data_frame_atualizado = data_frame_atualizado.withColumn(
    "classificacao_horas_escrita",
    when(col("tempoHoras") < 1, "Menos de uma hora")
    .when((col("tempoHoras") >= 1) & (col("tempoHoras") <= 1.5), "Uma hora a uma hora e meia")
    .when((col("tempoHoras") > 1.5) & (col("tempoHoras") <= 2.5), "Duas horas a duas horas e meia")
    .when((col("tempoHoras") > 2.5) & (col("tempoHoras") <= 3.5), "Três horas a três horas e meia")
    .otherwise("Mais de três horas e meia")
)

# Faz uma coluna de classificação do ano de lançamento em intervalos de 5 anos
data_frame_atualizado = data_frame_atualizado.withColumn(
    "classificacao_ano",
    floor(col("anoLancamento") / 5) * 5
)

# Faz uma coluna de classificação da nota média dos filmes
data_frame_atualizado = data_frame_atualizado.withColumn(
    "classificacao_nota_numerica",
    when((col("notaMedia") > 0) & (col("notaMedia") < 1), 1)
    .when((col("notaMedia") >= 1) & (col("notaMedia") < 2), 2)
    .when((col("notaMedia") >= 2) & (col("notaMedia") < 3), 3)
    .when((col("notaMedia") >= 3) & (col("notaMedia") < 4), 4)
    .when((col("notaMedia") >= 4) & (col("notaMedia") < 5), 5)
    .when((col("notaMedia") >= 5) & (col("notaMedia") < 6), 6)
    .when((col("notaMedia") >= 6) & (col("notaMedia") < 7), 7)
    .when((col("notaMedia") >= 7) & (col("notaMedia") < 8), 8)
    .when((col("notaMedia") >= 8) & (col("notaMedia") < 9), 9)
    .when((col("notaMedia") >= 9) & (col("notaMedia") <= 10), 10)
    .otherwise(0)  
)

# Faz uma coluna de classificação da nota média dos filmes
data_frame_atualizado = data_frame_atualizado.withColumn(
    "classificacao_nota_escrita",
    when((col("notaMedia") >= 1) & (col("notaMedia") < 2), "1 a menos de 2")
    .when((col("notaMedia") >= 2) & (col("notaMedia") < 3), "2 a menos de 3")
    .when((col("notaMedia") >= 3) & (col("notaMedia") < 4), "3 a menos de 4")
    .when((col("notaMedia") >= 4) & (col("notaMedia") < 5), "4 a menos de 5")
    .when((col("notaMedia") >= 5) & (col("notaMedia") < 6), "5 a menos de 6")
    .when((col("notaMedia") >= 6) & (col("notaMedia") < 7), "6 a menos de 7")
    .when((col("notaMedia") >= 7) & (col("notaMedia") < 8), "7 a menos de 8")
    .when((col("notaMedia") >= 8) & (col("notaMedia") < 9), "8 a menos de 9")
    .when((col("notaMedia") >= 9) & (col("notaMedia") <= 10), "9 a 10")
    .otherwise("Sem nota")  
)

# Faz uma coluna de classificação do numero de votos 
data_frame_atualizado = data_frame_atualizado.withColumn(
    "classificacao__votos_escrita",
    when((col("numeroVotos") >= 1) & (col("numeroVotos") <= 50), "1 - 50 votos")
    .when((col("numeroVotos") > 50) & (col("numeroVotos") <= 100), "51 - 100 votos")
    .when((col("numeroVotos") > 100) & (col("numeroVotos") <= 500), "101 - 500 votos")
    .when((col("numeroVotos") > 500) & (col("numeroVotos") <= 1000), "501 - 1000 votos")
    .when((col("numeroVotos") > 1000) & (col("numeroVotos") <= 2000), "1001 - 2000 votos")
    .when((col("numeroVotos") > 2000) & (col("numeroVotos") <= 3000), "2001 - 3000 votos")
    .when((col("numeroVotos") > 3000) & (col("numeroVotos") <= 5000), "3001 - 5000 votos")
    .when(col("numeroVotos") > 5000, "Mais de 5000 votos")
    .otherwise("Sem votos")
)

colunas_ordenadas = ["id", "tituloPrincipal", "tituloOriginal", "anoLancamento",  "classificacao_ano", "tempoMinutos", "tempoHoras", "classificacao_horas_numerica", "classificacao_horas_escrita", "genero", "notaMedia",  "classificacao_nota_escrita",   "classificacao_nota_numerica", "numeroVotos", "classificacao__votos_escrita", "generoArtista", "personagem", "nomeArtista", "anoNascimento",  "anoFalecimento", "profissao"] 

                       
data_frame_atualizado = data_frame_atualizado.select(colunas_ordenadas)

for column in data_frame_atualizado.columns: # Corrige outros valores nulos
    data_frame_atualizado = data_frame_atualizado.withColumn(column, when(col(column) == "\\N", None).otherwise(col(column)))
    data_frame_atualizado = data_frame_atualizado.withColumn(column, when(col(column) == "null", None).otherwise(col(column)))
    
data_frame_atualizado = data_frame_atualizado.withColumn("notaMedia", col("notaMedia").cast("double")) # Transforma os dados da coluna em double para
data_frame_atualizado = data_frame_atualizado.withColumn("notaMedia", format_number(col("notaMedia"), 1)) # arrendodar em uma casa decimal após o '.'

dynamic_frame = DynamicFrame.fromDF(data_frame_atualizado, glueContext, "dynamic_frame_name")

glueContext.write_dynamic_frame.from_options( # Envia os dados para o destino no formato parquet
    frame = dynamic_frame,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "parquet"
)     

 
job.commit()

# SERIES DO TMDB

# Os dados dos arquivo_*.json (provindo da chamada a api do TMDB) da camada Raw estão sendo tradados e enviados para a Trusted

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import when, col, format_number

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

source_file = "s3://dados-desafio/Raw/TMDB/JSON/Series/2023/10/27/arquivo_*.json" # Local do arquivo_*.json
target_path = "s3://dados-desafio/Trusted/TMDB/Series/2023/10/27/" # Destino dos dados tratados

data_frame = spark.read.json(source_file)

colunas_ordenadas = ["id", "tituloPrincipal", "tituloOriginal", "anoLancamento", "tempoMinutos",
                      "genero", "notaMedia", "numeroVotos", "generoArtista", "personagem", "nomeArtista", 
                      "anoNascimento",  "anoFalecimento", "profissao"]

data_frame = data_frame.select(colunas_ordenadas) # Ordena as colunas

for column in data_frame.columns: # Trata os dados nulos
    data_frame = data_frame.withColumn(column, when((col(column).isNull()) | (col(column) == "null"), "NULL").otherwise(col(column)))

data_frame = data_frame.withColumn("notaMedia", col("notaMedia").cast("double"))
data_frame = data_frame.withColumn("notaMedia", format_number(col("notaMedia"), 1))

dynamic_frame = DynamicFrame.fromDF(data_frame, glueContext, "dynamic_frame_name")

glueContext.write_dynamic_frame.from_options( # Envia para o destino no formato parquet
    frame = dynamic_frame,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "parquet"
    )   

job.commit()

   