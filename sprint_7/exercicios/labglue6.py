# Apresentar qual foi o nome feminino com mais registros e em que ano ocorreu #

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import count, desc

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

data_frame = spark.read.csv(source_file, header=True, inferSchema=True)

sexo_feminino = data_frame.filter(data_frame['sexo'] == 'F')

contagem_nomes_femininos = sexo_feminino.groupBy('nome').count()

nome_mais_registros = contagem_nomes_femininos.orderBy(desc('count')).head()["nome"]

dados_nome_mais_registros = sexo_feminino.filter(sexo_feminino['nome'] == nome_mais_registros)

ano_ocorrencia = dados_nome_mais_registros.orderBy('ano').head()['ano']

print("O nome feminino mais comum é: {} e ocorreu no ano: {}".format(nome_mais_registros, ano_ocorrencia))

job.commit()