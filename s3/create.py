import boto3
import os
from dotenv import load_dotenv
load_dotenv()
bucket_name = os.environ.get('bucket_name')

resource = boto3.resource('s3')
bucket = resource.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}
    )
print(bucket)