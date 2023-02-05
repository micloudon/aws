import boto3

ec2 = boto3.resource('ec2')

ec2_client = boto3.client("ec2", region_name="us-west-2")
response = ec2_client.stop_instances(InstanceIds=[])
print(response)