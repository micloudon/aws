import boto3

ec2 = boto3.resource('ec2')

# Launches an EC2 instance
instances = ec2.create_instances(
        # ubuntu 22.04
        ImageId="ami-095413544ce52437d",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="KeyPair1"
    )