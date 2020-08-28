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
