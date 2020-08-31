import uuid, boto3

dynamo = boto3.client("dynamodb", region_name='us-east-1')
target = 'COLLECTION'
tableName ='NajaraCollections'
attributes=['name', 'description']

#DEVELOPMENT: create table if it doesn't exist
#try:
#    response = dynamo.describe_table(TableName=tableName)
#except dynamo.exceptions.ResourceNotFoundException:
#    response = dynamo.create_table(
#        AttributeDefinitions=[
#            {
#                'AttributeName': 'id',
#                'AttributeType': 'S'
#            }
#        ],
#        TableName=tableName,
#        KeySchema=[
#            {
#                'AttributeName': 'id',
#                'KeyType': 'HASH'
#            }
#        ],
#        BillingMode='PAY_PER_REQUEST')
#    pass

def listAll():
    response = dynamo.scan(
            TableName=tableName
    )
    def unwrap_dynamo_output(text):
        print(text)
        text['id'] = text['id']['S']
        text['name'] = text['name']['S']
        text['description'] = text['description']['S']
        return text
    items = response['Items']
    unwrapped_items = map(unwrap_dynamo_output, items)
    return { 'collections': list(unwrapped_items) }

def create(data):
    action = 'CREATE'
    
    resultId = str(uuid.uuid4())
    name = data.get('name', '-')
    description = data.get('description', '-')

    response = dynamo.put_item(
            TableName=tableName,
            Item={
                'id': { 'S': resultId },
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


def read(guid):
    response = dynamo.get_item(
            TableName=tableName,
            Key={
                'id': {
                    'S': guid
                    }
                },
            AttributesToGet=['id', 'name', 'description'],
            ConsistentRead=False
        )
    return {
            "collection" : {
                "id": response['Item']['id']['S'],
                "name": response['Item']['name']['S'],
                "description": response['Item']['description']['S']
                },
            "items": []
            }

def update(data, collection):
    action = 'UPDATE'
    actionSuccess = False
    expression = "SET "
    values = {}

    itemKey = {
            'id': { 'S': collection }
            }
    
    for key in data:
        if key.lower() in attributes:
            #add key and data to boto3 dynamo update expression
            expression += key.lower() + "= :" + key + ','
            values[':'+key] = {"S":str(data[key])}

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
            'result-id':collection
            }
