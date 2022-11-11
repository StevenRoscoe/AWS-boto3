#Ex 1:
ec2.Instance('<IMAGE ID>').start()


#Ex 2:
response = client.start_instances(
    InstanceIds=[
        '<INSTANCE ID>',
    ],
    
)