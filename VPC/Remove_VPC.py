import boto3

client=boto3.client("ec2")

response = client.delete_vpc(
    VpcId='vpc-019af2eae74e065c4'
    
)