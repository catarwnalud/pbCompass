#Escrever o código necessário para alterar a caixa dos valores da coluna nome para MAIÚSCULO#

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

df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [
            source_file
        ]
    },
    "csv",
    {"withHeader": True, "separator":","},
    )
    
mapping = [
    ("nome", "string", "nome", "string"),
    ("sexo", "string", "sexo", "string"),
    ("ano", "int", "ano", "int")
]

data_frame = df.toDF()
data_frame = data_frame.withColumn("nome", upper(col("nome")))
data_frame.show()
df2 = DynamicFrame.fromDF(data_frame, glueContext, "dynamic_frame")

glueContext.write_dynamic_frame.from_options(
    frame = df2,
    connection_type = "s3",
    connection_options = {"path": target_path},
    format = "csv")

job.commit()