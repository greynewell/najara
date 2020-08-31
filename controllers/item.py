import uuid, boto3, random
from chalice import NotFoundError

dynamo = boto3.client("dynamodb", region_name='us-east-1')
target = 'ITEM'
tableName ='NajaraItems'
attributes = ['id', 'name', 'type', 'quantity', 'weight', 'gpvalue', 'description']

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
    
    response = _put(data, resultId, collection)
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
            AttributesToGet=attributes,
            ConsistentRead=False
        )
    try:
        item = response['Item']
        return {
                'id':item['id']['N'],
                'name':item['name']['S'],
                'type':item['type']['S'],
                'quantity':int(item['quantity']['N']),
                'weight':float(item['weight']['N']),
                'gpvalue':float(item['gpvalue']['N']),
                'description':item['description']['S']
                }
    except Exception:
        raise NotFoundError("The requested item could not be found within the given collection.")

def update(data, item, collection):
    action = 'UPDATE'
    actionSuccess = False
    expression = "SET "
    values = {}

    itemKey = {
            'id': { 'N': str(item) },
            'collection': { 'S': collection}
            }
    
    for key in data:
        if key.lower() in attributes:
            #add key and data to boto3 dynamo update expression
            expression += key.lower() + "= :" + key + ','
            typeChar = "N"
            if isinstance(data[key], str):
                typeChar = "S"
            values[':'+key] = {typeChar:str(data[key])}

    response = dynamo.update_item(
        TableName=tableName,
        Key=itemKey,
        UpdateExpression=expression[:-1],
        ExpressionAttributeValues=values
    )
    actionSuccess = response['ResponseMetadata']['HTTPStatusCode'] == 200
    
    return {
            'action':action,
            'target':target,
            'success':actionSuccess,
            'result-id':item
            }

def delete(item, collection):
    action = 'DELETE'
    actionSuccess = False
    itemKey = {
            'id': { 'N': str(item) },
            'collection': { 'S': collection}
            }
    
    response = dynamo.delete_item(
            TableName=tableName,
            Key=itemKey
    )
    actionSuccess = response['ResponseMetadata']['HTTPStatusCode'] == 200

    return {
            'action':action,
            'target':target,
            'success':actionSuccess,
            'result-id':item
            }

def _put(data, item, collection):
    name = data.get('name', '-')
    description = data.get('description', '-')
    itemType = data.get('type', 'NotSpecified')
    quantity = data.get('quantity', 1)
    weight = data.get('weight', 0)
    gpvalue = data.get('gpvalue', 0)


    response = dynamo.put_item(
            TableName=tableName,
            Item={
                'id': { 'N': str(item) },
                'collection': { 'S': collection},
                'name': { 'S': name},
                'type': { 'S': itemType },
                'quantity': { 'N': str(quantity) },
                'weight': { 'N': str(weight) },
                'gpvalue': { 'N': str(gpvalue) },
                'description': { 'S': description}
                })
    return response
