import boto3  #Imports boto3, the SDK for python from AWS

dynamodb = boto3.resource('dynamodb')  #DynamoDB variable created that will call boto3's dynamoDB's resource.

table = dynamodb.create_table(     #Create_table  from boto3 that Creates our table.
    TableName='',   #Give your table a name
    KeySchema=[    #DynamoDB Key Schema, 
        {
            'AttributeName': 'Title',  #Name of your partition key
            'KeyType': 'HASH'  #Partition key  is required
        },
        {
            'AttributeName': 'Genre',   #Name of sort key
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Title',    #Reenter partition key and state whether it is a string, number, boolean (S|N|B)
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Genre', #Reenter your sort key and indicate whether it's a string, number, or boolean (S|N|B)
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={     #How quickly the table uploads the data
        'ReadCapacityUnits': 1,  #If you have more data, increase the amount of RCU's/WCU's
        'WriteCapacityUnits': 1
    }
)

print("Table status:", table.table_status)  #Display message that the table is being created.

print('Waiting for', table.name, 'to complete creating...')
table.meta.client.get_waiter('table_exists').wait(TableName=' ')
print('Table status:', dynamodb.Table(' ').table_status)