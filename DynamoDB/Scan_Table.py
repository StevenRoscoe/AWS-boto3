import boto3
import json  #Must iumport json becuase that is the format the scan will return in. 
dynamodb = boto3.client('dynamodb')

response = dynamodb.scan(
TableName=' '  #Table name is all we need here.
    )

for i in response['Items']:  #For loop that will print the json output in a list format.
    print(json.dumps(i))