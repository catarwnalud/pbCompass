import boto3
import csv
import datetime

aws_access_key_id = ''
aws_secret_access_key = ''
bucket_name = ''
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

local_movies_file = 'movies.csv'
local_series_file = 'series.csv'

raw_layer = 'Raw'
local_data = 'Local'
data_format = 'CSV'
data_specifications = ['Movies', 'Series']

today = datetime.date.today()
year = today.year
month = today.month
day = today.day

def upload_to_s3(local_file, data_specification):
    s3_key = f'{raw_layer}/{local_data}/{data_format}/{data_specification}/{year}/{month}/{day}/{data_specification.lower()}.csv'
    s3.upload_file(local_file, bucket_name, s3_key)

upload_to_s3(local_movies_file, data_specifications[0])
upload_to_s3(local_series_file, data_specifications[1])
