import boto3

dynamodb = boto3.client('dynamodb')

DELETE_TABLE = input("What is the name of the table to delete?: ") #user input to ask which table to delete

response = dynamodb.delete_table(
    TableName=DELETE_TABLE
)