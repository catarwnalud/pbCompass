#MOVIES CSV:

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

source_file = "s3://dados-desafio/Raw/Local/JSON/Movies/2023/10/27/arquivo_*.json"
target_path = "s3://dados-desafio/Trusted/Movies/"

data_frame = spark.read.json(source_file)

colunas_ordenadas = ["id", "tituloPincipal", "tituloOriginal", "anoLancamento", "tempoMinutos", "genero", "notaMedia", "numeroVotos", "generoArtista", "personagem", "nomeArtista", "anoNascimento",  "anoFalecimento", "profissao", "titulosMaisConhecidos"]

data_frame = data_frame.select(colunas_ordenadas)

data_frame = data_frame.withColumnRenamed("tituloPincipal", "tituloPrincipal") 

for column in data_frame.columns:
   data_frame = data_frame.withColumn(column, when(col(column) == "\\N", "NULL").otherwise(col(column)))
   
dynamic_frame = DynamicFrame.fromDF(data_frame, glueContext, "dynamic_frame_name")

glueContext.write_dynamic_frame.from_options(
    frame = dynamic_frame,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "parquet"
    )     
   
job.commit()

#SERIES CSV:

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

source_file = "s3://dados-desafio/Raw/Local/JSON/Series/2023/10/27/arquivo_*.json"
target_path = "s3://dados-desafio/Trusted/Series/"

data_frame = spark.read.json(source_file)

colunas_ordenadas = ["id", "tituloPincipal", "tituloOriginal", "anoLancamento", "tempoMinutos", "genero", "notaMedia", "numeroVotos", "generoArtista", "personagem", "nomeArtista", "anoNascimento",  "anoFalecimento", "profissao", "titulosMaisConhecidos"]

data_frame = data_frame.select(colunas_ordenadas)

data_frame = data_frame.withColumnRenamed("tituloPincipal", "tituloPrincipal") 

for column in data_frame.columns:
   data_frame = data_frame.withColumn(column, when(col(column) == "\\N", "NULL").otherwise(col(column)))
   
dynamic_frame = DynamicFrame.fromDF(data_frame, glueContext, "dynamic_frame_name")

glueContext.write_dynamic_frame.from_options(
    frame = dynamic_frame,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "parquet"
    )     
   
   
job.commit()


# MOVIES TMDB

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

source_file = "s3://dados-desafio/Raw/TMDB/JSON/Movies/2023/10/27/arquivo_*.json"
target_path = "s3://dados-desafio/Trusted/TMDB/Movies/2023/10/27/"

data_frame = spark.read.json(source_file)

colunas_ordenadas = ["id", "tituloPrincipal", "tituloOriginal", "anoLancamento", "tempoMinutos", "genero", "notaMedia", "numeroVotos", "generoArtista", "personagem", "nomeArtista", "anoNascimento",  "anoFalecimento", "profissao"]

data_frame = data_frame.select(colunas_ordenadas)

for column in data_frame.columns:
    data_frame = data_frame.withColumn(column, when((col(column).isNull()) | (col(column) == "null"), "NULL").otherwise(col(column)))

data_frame = data_frame.withColumn("notaMedia", col("notaMedia").cast("double"))
data_frame = data_frame.withColumn("notaMedia", format_number(col("notaMedia"), 1))

dynamic_frame = DynamicFrame.fromDF(data_frame, glueContext, "dynamic_frame_name")

glueContext.write_dynamic_frame.from_options(
    frame = dynamic_frame,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "parquet"
    )     

job.commit()

   

# SERIES TMDB

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

source_file = "s3://dados-desafio/Raw/TMDB/JSON/Series/2023/10/27/arquivo_*.json"
target_path = "s3://dados-desafio/Trusted/TMDB/Series/2023/10/27/"

data_frame = spark.read.json(source_file)

colunas_ordenadas = ["id", "tituloPrincipal", "tituloOriginal", "anoLancamento", "tempoMinutos", "genero", "notaMedia", "numeroVotos", "generoArtista", "personagem", "nomeArtista", "anoNascimento",  "anoFalecimento", "profissao"]

data_frame = data_frame.select(colunas_ordenadas)

for column in data_frame.columns:
    data_frame = data_frame.withColumn(column, when((col(column).isNull()) | (col(column) == "null"), "NULL").otherwise(col(column)))

data_frame = data_frame.withColumn("notaMedia", col("notaMedia").cast("double"))
data_frame = data_frame.withColumn("notaMedia", format_number(col("notaMedia"), 1))

dynamic_frame = DynamicFrame.fromDF(data_frame, glueContext, "dynamic_frame_name")

glueContext.write_dynamic_frame.from_options(
    frame = dynamic_frame,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "parquet"
    )   

job.commit()

   