"""

Usando a AWS Lambda foi filtrado os arquivos 'movies' e 'series' .csv pelo gênero 'War' ou 'Crime', foram transformados os campos '\n' 
em NULL e mandados os arquivos em formato json com 100 registros cada um para o bucket no caminho 
Raw/Local/JSON/Series/2023/10/27/arquivo_{i}.json

"""

# Movies

import boto3
import pandas as pd
import s3fs

def lambda_handler(event, context):
    
    s3_client = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')

    s3_path ='dados-desafio/Raw/Local/CSV/Movies/2023/10/16/movies.csv'

    s3 = s3fs.S3FileSystem(anon=False, key='', secret='')

    with s3.open(f's3://{s3_path}', 'rb') as file:
      
        df = pd.read_csv(file, delimiter='|')

        filmes_filtrado = df[(df['genero'] == 'War') | (df['genero'] == 'Crime')]

        filmes_filtrado = filmes_filtrado.replace(r'\N', 'NULL')

        lista_df = [filmes_filtrado[i:i+100] for i in range(0, len(filmes_filtrado), 100)]

        for i, conteudo in enumerate(lista_df):

            json = conteudo.to_json(orient='records')

            s3_path = f'Raw/Local/JSON/Movies/2023/10/27/arquivo_{i}.json'

            s3_client.put_object(Body=json, Bucket='dados-desafio', Key=s3_path)

            print(f'Arquivo {i} enviado para o S3: {s3_path}')

    return 'Processamento concluido'

print(lambda_handler('a','b'))

# Series

import boto3
import pandas as pd
import s3fs

def lambda_handler(event, context):
    
    s3_client = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')

    s3_path = 'dados-desafio/Raw/Local/CSV/Series/2023/10/16/series.csv'

    s3 = s3fs.S3FileSystem(anon=False, key='', secret='')

    with s3.open(f's3://{s3_path}', 'rb') as file:
      
        df = pd.read_csv(file, delimiter='|')

        filmes_filtrado = df[(df['genero'] == 'War') | (df['genero'] == 'Crime')]

        filmes_filtrado = filmes_filtrado.replace(r'\N', 'NULL')

        lista_df = [filmes_filtrado[i:i+100] for i in range(0, len(filmes_filtrado), 100)]

        for i, conteudo in enumerate(lista_df):

            json = conteudo.to_json(orient='records')

            s3_path = f'Raw/Local/JSON/Series/2023/10/27/arquivo_{i}.json'

            s3_client.put_object(Body=json, Bucket='dados-desafio', Key=s3_path)

            print(f'Arquivo {i} enviado para o S3: {s3_path}')

    return 'Processamento concluido'

print(lambda_handler('a','b'))



