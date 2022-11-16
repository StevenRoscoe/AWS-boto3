import boto3

dynamodb = boto3.resource('dynamodb')  #DynamoDB variable created that will call boto3's dynamoDB's resource.

Video_Games = [    #List for our table:
    {'Title': " ", "Genre":" "},
    {'Title': " ", "Genre":" "},
    {'Title': " ", "Genre":" "},
    {'Title': " ", "Genre":" "},
    {'Title': " ", "Genre":" "},
    {'Title': " ", "Genre":" "},
    {'Title': " ", "Genre":" "},
    {'Title': " ", "Genre":" "},
    {'Title': " ", "Genre":" "},
    {'Title': " ", "Genre":" "},
        ]
    
table = dynamodb.Table("<TABLE NAME> ") #Creates a variable, table, that calls our table name
with table.batch_writer() as batch:   #Batch writer that uploads multiple items to the DynamoDB
    for Title in Video_Games:
        batch.put_item(
            Item=Title
            )