import boto3

#Create an S3 bucket:

client = boto3.client("s3")

client.create_bucket(Bucket="sroscoe")


#Another way to create an S3 bucket (public):
import boto3
aws_resource=boto3.resource('s3')
bucket=aws_resource.Bucket("<BUCKET NAME>")         #Name your bucket

response = bucket.create(
    ACL='public-read'
)

print(response)


#Private bucket
import boto3
aws_resource=boto3.resource('s3')
bucket=aws_resource.Bucket("<BUCKET NAME>")         #Name your bucket

response = bucket.create(
    ACL='private'
)

print(response)