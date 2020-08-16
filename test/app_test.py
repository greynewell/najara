import json
import pytest
from app import app


@pytest.fixture
def gateway_factory():
    from chalice.config import Config
    from chalice.local import LocalGateway

    def create_gateway(config=None):
        if config is None:
            config = Config()
        return LocalGateway(app, config)
    return create_gateway


class TestChalice(object):
    def test_createCollection(self, gateway_factory):
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

