# MOVIES CSV/TMDB

# Usando os arquivos tratados da camada Trusted, foi unido os dados de filmes, feito a modelagem dimensional e mandado para a camada
# Refined, onde os dados estão prontos para serem utilizados na análise.


import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

path_movies_csv = 's3://dados-desafio/Trusted/Movies/'  # Local na Trusted dos arquivos de filmes provindos do CSV
path_movies_tmdb = 's3://dados-desafio/Trusted/TMDB/Movies/2023/10/27/'  # Local na Trusted dos arquivos de filmes provindos do TMDB

output_path = 's3://dados-desafio/Refined/Movies/' # Destino dos dados na Refined

df_movies_csv = spark.read.parquet(path_movies_csv)
df_movies_tmdb = spark.read.parquet(path_movies_tmdb)

# Seleção das colunas necessárias para minha análise 
df_movies_csv = df_movies_csv.select(['id', 'tituloPrincipal', 'tituloOriginal', 'anoLancamento', 'tempoMinutos',
                                       'genero', 'notaMedia', 'numeroVotos'])
df_movies_tmdb = df_movies_tmdb.select(['id', 'tituloPrincipal', 'tituloOriginal', 'anoLancamento', 'tempoMinutos', 
                                        'genero', 'notaMedia', 'numeroVotos'])

df_movies = df_movies_csv.union(df_movies_tmdb) # União dos dados do CSV e do TMDB

df_movies = df_movies.dropDuplicates(['tituloPrincipal', 'tituloOriginal']) # Eliminação dos dados repetidos

df = df_movies.select(['id', 'tituloPrincipal', 'tituloOriginal', 'genero', 'anoLancamento',
                        'notaMedia', 'numeroVotos', 'tempoMinutos']) 

# Envio de ambos para a pasta 'Movies/' da Refined
df.write.mode('overwrite').csv(output_path)

job.commit()

# SERIES CSV/TMDB

# Usando os arquivos tratados da camada Trusted, foi unido os dados de series, feito a modelagem dimensional e mandado para a camada
# Refined, onde os dados estão prontos para serem utilizados na análise.

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

path_series_csv = 's3://dados-desafio/Trusted/Series/' # Local na Trusted dos arquivos de series provindos do CSV
path_series_tmdb = 's3://dados-desafio/Trusted/TMDB/Series/2023/10/27/' # Local na Trusted dos arquivos de series provindos do TMDB

output_path_dim = 's3://dados-desafio/Refined/Series/Dim_series/' # Destino dos dados considerados dimensionais na Refined
output_path_fato = 's3://dados-desafio/Refined/Series/Fato_series/' # Destino dos dados considerados fatos na Refined

df_series_csv = spark.read.parquet(path_series_csv)
df_series_tmdb = spark.read.parquet(path_series_tmdb)

# Seleção das colunas necessárias para minha análise 
df_series_csv = df_series_csv.select(['id', 'tituloPrincipal', 'tituloOriginal', 'anoLancamento', 
                                      'tempoMinutos', 'genero', 'notaMedia', 'numeroVotos'])
df_series_tmdb = df_series_tmdb.select(['id', 'tituloPrincipal', 'tituloOriginal', 'anoLancamento',
                                         'tempoMinutos', 'genero', 'notaMedia', 'numeroVotos'])

df_series = df_series_csv.union(df_series_tmdb) # União dos dados do CSV e do TMDB

df_series = df_series.dropDuplicates(['tituloPrincipal', 'tituloOriginal']) # Eliminação dos dados repetidos

# Modelagem Dimensional
dim_series = df_series.select(['id', 'tituloPrincipal', 'tituloOriginal', 'genero', 'anoLancamento']) # Colunas considerados dimensionais
fato_series = df_series.select(['tituloPrincipal', 'tituloOriginal', 'notaMedia', 'numeroVotos', 'tempoMinutos']) # Colunas considerados fatos


# Envio de ambos para a pasta 'Series/' da Refined
dim_series.write.mode('overwrite').csv(output_path_dim)
fato_series.write.mode('overwrite').csv(output_path_fato)

job.commit()