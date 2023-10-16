# Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo.
# Ordene os dados de modo que o ano mais recente apareça como primeiro registro do dataframe.


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

contagem_nomes = data_frame.groupBy('ano', 'sexo').agg(count('nome'))

contagem_nomes = contagem_nomes.orderBy(desc('ano'))

contagem_nomes.show()

job.commit()