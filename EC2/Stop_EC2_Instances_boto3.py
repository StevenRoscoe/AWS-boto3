#Ex 1:
ec2.Instance('<IMAGE ID>').stop()
ec2.Instance('<IMAGE ID>').stop()
ec2.Instance('<IMAGE ID>').stop()


#Ex 2:
response = client.stop_instances(
    InstanceIds=[
        '<INSTANCE ID>',
    ],
    
)