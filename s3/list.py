import boto3

client = boto3.client("s3")
response = client.list_buckets()

print("Listing Amazon S3 Buckets:")
for bucket in response['Buckets']:
    print(f"-- {bucket['Name']}")