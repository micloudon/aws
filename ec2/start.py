import boto3
import os
from dotenv import load_dotenv
load_dotenv()
instance_id = os.environ.get('instance_id')

ec2 = boto3.client('ec2')

response = ec2.start_instances(InstanceIds=[instance_id])

print(response)