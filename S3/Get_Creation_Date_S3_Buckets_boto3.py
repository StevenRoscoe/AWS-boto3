#Gets the name and timestamp of creation date of all S3 buckets:
import boto3

s3_resource=boto3.client("s3")

for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])