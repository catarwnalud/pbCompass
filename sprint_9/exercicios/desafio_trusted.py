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
from pyspark.sql.functions import when, col

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

colunas_ordenadas = ["id", "tituloPincipal", "tituloOriginal", "anoLancamento", "tempoMinutos", "genero", "notaMedia", 
                     "numeroVotos", "generoArtista", "personagem", "nomeArtista", "anoNascimento",  "anoFalecimento", "profissao",
                       "titulosMaisConhecidos"] 

data_frame = data_frame.select(colunas_ordenadas) # Ordena as colunas

data_frame = data_frame.withColumnRenamed("tituloPincipal", "tituloPrincipal") # Trata erro do nome da coluna

for column in data_frame.columns: # Trata os dados nulos
   data_frame = data_frame.withColumn(column, when(col(column) == "\\N", "NULL").otherwise(col(column)))
   
dynamic_frame = DynamicFrame.fromDF(data_frame, glueContext, "dynamic_frame_name")

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

for column in data_frame.columns: # Trata os arquivos nulos
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
from pyspark.sql.functions import when, col, format_number

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

source_file = "s3://dados-desafio/Raw/TMDB/JSON/Movies/2023/10/27/arquivo_*.json" # Local dos arquivos
target_path = "s3://dados-desafio/Trusted/TMDB/Movies/2023/10/27/" # Destino dos dados tratados

data_frame = spark.read.json(source_file)

colunas_ordenadas = ["id", "tituloPrincipal", "tituloOriginal", "anoLancamento", "tempoMinutos",
                      "genero", "notaMedia", "numeroVotos", "generoArtista", "personagem", "nomeArtista", "anoNascimento", 
                        "anoFalecimento", "profissao"]

data_frame = data_frame.select(colunas_ordenadas) # Ordena as colunas

for column in data_frame.columns: # Trata os dados nulos
    data_frame = data_frame.withColumn(column, when((col(column).isNull()) | (col(column) == "null"), "NULL").otherwise(col(column)))

data_frame = data_frame.withColumn("notaMedia", col("notaMedia").cast("double")) # Transforma os dados da coluna em double para
data_frame = data_frame.withColumn("notaMedia", format_number(col("notaMedia"), 1)) # arrendodar em uma casa decimal após o '.'

dynamic_frame = DynamicFrame.fromDF(data_frame, glueContext, "dynamic_frame_name")

glueContext.write_dynamic_frame.from_options( # Envia os dados para o destino
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

source_file = "s3://dados-desafio/Raw/TMDB/JSON/Series/2023/10/27/arquivo_*.json" # Local dos arquivos
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

   