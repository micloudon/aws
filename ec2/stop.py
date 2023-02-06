import boto3
import os
from dotenv import load_dotenv
load_dotenv()
instance_id = os.environ.get('instance_id')


ec2 = boto3.resource('ec2')

ec2_client = boto3.client("ec2", region_name="us-west-2")
response = ec2_client.stop_instances(InstanceIds=[instance_id])
print(response)