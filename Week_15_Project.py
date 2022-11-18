import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Create a SQS queue
response = sqs.create_queue(
    QueueName='Week_15',
    Attributes={
        'DelaySeconds': '60',
        'MessageRetentionPeriod': '86400'
    }
)

print(response['QueueUrl'])


#Lambda Code
import json                                 #transfers data into the JSON format
import boto3                                #imports AWS' Python SDK into the code so it will run
from datetime import datetime               #allows us to get the time and send it in a message

def lambda_handler(event, context):         #the function starts here
 
    now = datetime.now()                    #assigned the variable 'now' to the datetime.now() method that gives the current time
    time = now.strftime("%H:%M:%S ")        #will give us back the current time in hours, minutes, and seconds

    sqs = boto3.client('sqs')               #code needed to call on the resource 'SQS'
    
    sqs.send_message(QueueUrl="https://sqs.us-east-1.amazonaws.com/785610249674/Week_15",MessageBody=time)    #will send the message to the URL
    
    return {
        'statusCode': 200,                  #will return a status code of 200, letting us know that the code ran successfully
        'body': json.dumps('MISSION COMPLETE!!!!!')
    }