import boto3
import os
from dotenv import load_dotenv
load_dotenv()
bucket_name2 = os.environ.get('bucket_name2')


client = boto3.client("s3")
client.delete_bucket(Bucket=bucket_name2)
print("Amazon S3 Bucket has been deleted")