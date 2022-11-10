#Prints the names of all S3 buckets into a list in the account:
import boto3

resource=boto3.resource("s3")

print(list(resource.buckets.all()))


#Prints the service and names of all buckets in the account:
import boto3

resource=boto3.resource("s3")

for bucket in resource.buckets.all():
    print(bucket)
    

#Prints just the names of the buckets in the account:    
import boto3

resource=boto3.resource("s3")

for bucket in resource.buckets.all():
    print(bucket.name)