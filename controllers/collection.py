import uuid, boto3

dynamo = boto3.client("dynamodb", region_name='us-east-1')
target = 'COLLECTION'
tableName ='NajaraCollections'

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

