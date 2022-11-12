import boto3

ec2 = boto3.resource('ec2')
  
#instance = ec2.create_instances(   
    #ImageId='ami-09d3b3274b6c5d4aa',             
    #MinCount=6,                                        
    #MaxCount=6,                                                    
    #InstanceType='t2.micro',                    
#)                                   
#print(instance) 


instances = ec2.instances.filter(
    Filters = [{'Name': 'Development', 'Values': ['running']},
    {'Name':'tag:Development','Values':['true']}]
)
print(instances)