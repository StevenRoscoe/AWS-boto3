import boto3                        #For every snapshot

ec2_boto3=boto3.client("ec2")

ec2_boto3.describe_snapshots()      


import boto3                        #For a certain snapshot

ec2_boto3=boto3.client("ec2")

ec2_boto3.describe_snapshots(SnapshotIds=[
    ''
    ])