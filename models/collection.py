import uuid
import boto3

dynamo = boto3.client("dynamodb")
target = 'COLLECTION'
tableName ='NajaraCollections'

#check for table or create it
try:
    response = dynamo.describe_table(TableName=tableName)
except dynamo.exceptions.ResourceNotFoundException:
    response = dynamo.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        TableName=tableName,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        BillingMode='PAY_PER_REQUEST')
    pass

def getInput(data, key):
    userInput = "-"
    if hasattr(data, key):
        userInput = data[key]
    return userInput

def create(data):
    action = 'CREATE'
    resultId = str(uuid.uuid4())

    response = dynamo.put_item(
            TableName=tableName,
            Item={
                'id': { 'S': resultId },
                'name': { 'S': getInput(data, 'name')},
                'description': { 'S': getInput(data, 'description')}
                })
    actionSuccess = response['ResponseMetadata']['HTTPStatusCode'] == 200
    return {
            'action':action,
            'target':target,
            'success':actionSuccess,
            'result-id':resultId
            }
