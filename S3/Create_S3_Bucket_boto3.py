#We will use the following code to import boto3:
import boto3

#Create an S3 bucket:

client = boto3.client("s3")

client.create_bucket(Bucket="sroscoe")