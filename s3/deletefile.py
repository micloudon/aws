import boto3
import os
from dotenv import load_dotenv
load_dotenv()
bucket_name2 = os.environ.get('bucket_name2')


s3_resource = boto3.resource("s3")
object = s3_resource.Object(bucket_name2, key='WIN_20220728_20_55_00_Pro.jpg')
object.delete()