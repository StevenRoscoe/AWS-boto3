#Ex 1:
import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
)
print(instance)


#Ex 2:
import boto3

ec2 = boto3.resource('ec2')

ec2.create_instances(ImageId='<ami-image-id>', MinCount=1, MaxCount=5)


#Ex 3:
import boto3

client = boto3.client('ec2')