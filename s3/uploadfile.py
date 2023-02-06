import boto3
import os
from dotenv import load_dotenv
load_dotenv()
bucket_name = os.environ.get('bucket_name')


s3 = boto3.resource('s3')
s3.Bucket(bucket_name).upload_file('sample.txt', 'sample.txt')