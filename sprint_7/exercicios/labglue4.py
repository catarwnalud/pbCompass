#Imprimir a contagem de linhas presentes no dataframe#

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, upper
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import SparkSession

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
data_frame.show()
linhas = data_frame.count()
print('Número de linhas do dataFrame: ', linhas )


job.commit()