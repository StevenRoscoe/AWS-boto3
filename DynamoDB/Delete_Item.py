import boto3
dynamodb = boto3.client('dynamodb')

response = dynamodb.delete_item(
    TableName=' ', #item we want to delete
    Key=  {
        ' ': {"S": " "}, #title and genre strings of item to delete from table.
        " ": {"S": " "},
        }
)