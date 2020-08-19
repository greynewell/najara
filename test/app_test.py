import json, pytest, os, boto3
from moto import mock_dynamodb2
tableName='NajaraCollections'


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
        TableName=tableName,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
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


class TestChalice(object):
    def test_createCollection(self, gateway_factory, collection):
        gateway = gateway_factory()
        
        requestBody = {'name':'test', 'description':'testy'}
        response = gateway.handle_request(method='POST',
                                          path='/collection',
                                          headers={'Content-Type':
                                                   'application/json'},
                                          body='{"name":"test", "description":"testy"}')
        assert response['statusCode'] == 200
        responseBody = json.loads(response['body']) 
        assert responseBody['action'] == 'CREATE'
        assert responseBody['target'] == 'COLLECTION'
        assert responseBody['success'] == True
        assert len(responseBody['result-id'].split('-')) == 5
        collectionID = responseBody['result-id']
        getResponse = gateway.handle_request(method='GET',
                                          path='/collection/' + collectionID,
                                          headers={},
                                          body='')
        assert getResponse['statusCode'] == 200
        testCollection = json.loads(getResponse['body'])['collection']
        assert testCollection['name'] == 'test'
        assert testCollection['description'] == 'testy'

    def test_createItem(self, gateway_factory):
        gateway = gateway_factory()
        response = gateway.handle_request(method='POST',
                                          path='/item/some-fake-guid',
                                          headers={},
                                          body='')
        assert response['statusCode'] == 200
        assert json.loads(response['body']) == dict([('collection', 'some-fake-guid')])

