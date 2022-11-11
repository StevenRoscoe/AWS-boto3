import boto3

ec2 = boto3.resource('ec2')
                                           
instance = ec2.create_instances(    ############
    ImageId='ami-09d3b3274b6c5d4aa',        #################        
    MinCount=3,                                         ###################
    MaxCount=3,                                                     ####################Comment out these lines when running the code to stop the instances!
    InstanceType='t2.micro',                            ###################
)                                           #################
print(instance)                     ############

ec2.Instance('i-0c7c7b9fdbd10f7d5').stop()              #Stop Instances
ec2.Instance('i-05d0a145604b7773f').stop()
ec2.Instance('i-0c3ecab6b79a8951a').stop()