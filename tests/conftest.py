import json, pytest, os, boto3
from moto import mock_dynamodb2


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'

@pytest.fixture(scope='function')
def dynamodb(aws_credentials):
    with mock_dynamodb2():
        yield boto3.client('dynamodb', region_name='us-east-1')

@pytest.fixture(scope='function')
def collection(dynamodb):
    response = dynamodb.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        TableName='NajaraCollections',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ])
    return response

@pytest.fixture(scope='function')
def item(dynamodb):
    response = dynamodb.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'collection',
                'AttributeType': 'S'
            }
        ],
        TableName='NajaraItems',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'collection',
                'KeyType': 'RANGE'
            }
        ])
    return response

@pytest.fixture
def gateway_factory(dynamodb, collection):
    from chalice.config import Config
    from chalice.local import LocalGateway
    from app import app

    def create_gateway(config=None):
        if config is None:
            config = Config()
        return LocalGateway(app, config)
    return create_gateway

@pytest.fixture
def create_item(gateway_factory, item):
    gateway = gateway_factory()

    requestBody = {'name':'Arrow', 'description':'A regular wooden arrow.', 'type': 'Ammunition',
                    'quantity':1, 'weight':0.05, 'gpvalue':0.05}
    response = gateway.handle_request(method='POST', path='/item/test-collection-guid-for-item',
                                    headers={'Content-Type':'application/json'},
                                    body=json.dumps(requestBody))
    return response

@pytest.fixture
def create_response_body_json(create_item):
    return json.loads(create_item['body'])

@pytest.fixture
def get_created_item(create_response_body_json, gateway_factory):
    gateway = gateway_factory()
    itemID = create_response_body_json['result-id']
    response = gateway.handle_request(method='GET',
                                        path='/item/test-collection-guid-for-item/' + str(itemID),
                                        headers={},
                                        body='')
    return response

@pytest.fixture
def created_item(get_created_item):
    return json.loads(get_created_item['body'])

@pytest.fixture
def create_collection(gateway_factory, collection):
    gateway = gateway_factory()
    response = gateway.handle_request(method='POST', path='/collection',
                                    headers={'Content-Type':'application/json'},
                                    body='{"name":"test", "description":"testy"}')
    return response
