import uuid, boto3, random

dynamo = boto3.client("dynamodb", region_name='us-east-1')
target = 'ITEM'
tableName ='NajaraItems'

#DEVELOPMENT: create table if it doesn't exist
#try:
#    response = dynamo.describe_table(TableName=tableName)
#except dynamo.exceptions.ResourceNotFoundException:
#    response = dynamo.create_table(
#        AttributeDefinitions=[
#            {
#                'AttributeName': 'id',
#                'AttributeType': 'N'
#            },
#            {
#                'AttributeName': 'collection',
#                'AttributeType': 'S'
#            }
#        ],
#        TableName=tableName,
#        KeySchema=[
#            {
#                'AttributeName': 'id',
#                'KeyType': 'HASH'
#            },
#            {
#                'AttributeName': 'collection',
#                'KeyType': 'RANGE'
#            }
#        ],
#        BillingMode='PAY_PER_REQUEST')
#    pass

def create(data, collection):
    action = 'CREATE'
    
    resultId= random.randint(0, 10000000000000)

    name = data.get('name', '-')
    description = data.get('description', '-')
    itemType = data.get('type', 'NotSpecified')
    quantity = data.get('quantity', 1)
    weight = data.get('weight', 0)
    gpvalue = data.get('gpvalue', 0)


    response = dynamo.put_item(
            TableName=tableName,
            Item={
                'id': { 'N': str(resultId) },
                'collection' : { 'S': collection},
                'name': { 'S': name},
                'description': { 'S': description}
                })
    actionSuccess = response['ResponseMetadata']['HTTPStatusCode'] == 200
    return {
            'action':action,
            'target':target,
            'success':actionSuccess,
            'result-id':resultId
            }


def read(item, collection):
    response = dynamo.get_item(
            TableName=tableName,
            Key={
                'id': {
                    'N': item
                    },
                'collection': {
                    'S': collection
                    }
                },
            AttributesToGet=['id', 'name', 'description'],
            ConsistentRead=False
        )
    return {
                "id": response['Item']['id']['S'],
                "name": response['Item']['name']['S'],
                "description": response['Item']['description']['S']
            }

