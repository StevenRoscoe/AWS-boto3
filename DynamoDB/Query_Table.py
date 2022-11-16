import boto3
import json
from boto3.dynamodb.conditions import Key

TABLE_NAME = " "

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name="us-east-1")

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)
print(table)


response = table.query(KeyConditionExpression=Key('Title').eq('Pitfall')) #Make beginning query
TableName=TABLE_NAME,
KeyConditionExpression=Key('Title'),
ExpressionAttributeValues={':Title': 'Pitfall'}
print(response['Items'])