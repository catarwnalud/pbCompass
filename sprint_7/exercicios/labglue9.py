''' 
Escrever o conteúdo do dataframe com os valores de nome em maiúsculo no S3.

Atenção aos requisitos:
		
	- A gravação deve ocorrer no subdiretório frequencia_registro_nomes_eua do path s3://<BUCKET>/lab-glue/
	- O formato deve ser JSON
	- O particionamento deverá ser realizado pelas colunas sexo e ano (nesta ordem) 
'''

import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from pyspark.sql.functions import col, upper

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])
job_name = args['JOB_NAME']
input_path = args['S3_INPUT_PATH']
output_path = args['S3_TARGET_PATH']

sc = SparkContext()
glueContext = GlueContext(sc)
job = Job(glueContext)
job.init(job_name, args)

df = glueContext.create_dynamic_frame.from_options(
    connection_type='s3',
    connection_options={'paths': [input_path]},
    format='csv',
    format_options={'withHeader': True, 'separator': ','}
    )

mapping = [
    ('nome', 'string', 'nome', 'string'),
    ('sexo', 'string', 'sexo', 'string'),
    ('ano', 'int', 'ano', 'int')
]

data_frame = df.toDF()
data_frame = data_frame.withColumn('nome', upper(col('nome')))

df2 = DynamicFrame.fromDF(data_frame, glueContext, 'dynamic_frame')

glueContext.write_dynamic_frame.from_options(
    frame = df2,
    connection_type = 's3',
    connection_options = {'path' : output_path, 'partition_keys': ['sexo','ano']},
    format = 'json'
    )

job.commit()