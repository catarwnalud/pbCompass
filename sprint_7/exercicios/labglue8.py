# Apresentar o total de registros (masculinos e femininos) para cada ano presente no dataframe.
# Considere apenas as primeiras 10 linhas, ordenadas pelo ano, de forma crescente 

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from pyspark.sql import SparkSession
from pyspark.sql.functions import count, desc, col, upper


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

contagem_por_ano = data_frame.groupBy('ano', 'sexo').count()
contagem_ordenada = contagem_por_ano.orderBy('ano')
contagem_ordenada.show(10)

job.commit()