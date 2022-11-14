import boto3

ec2_client=boto3.client("ec2")

ec2_client.create_volume(AvailabilityZone='us--',
    Encrypted=True,
    Size=12,
    SnapshotId='',
    VolumeType='gp2')