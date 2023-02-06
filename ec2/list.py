import boto3

ec2 = boto3.resource('ec2')
    
ec2_client = boto3.client("ec2")
instances = ec2_client.describe_instances(
        Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
            
        }
    ]

)

print(instances)