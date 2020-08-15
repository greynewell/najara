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
        response = gateway.handle_request(method='POST',
                                          path='/collection',
                                          headers={},
                                          body='')
        assert response['statusCode'] == 200
        responseBody = json.loads(response['body']) 
        assert responseBody['action'] == 'createCollection'

    def test_createItem(self, gateway_factory):
        gateway = gateway_factory()
        response = gateway.handle_request(method='POST',
                                          path='/item/some-fake-guid',
                                          headers={},
                                          body='')
        assert response['statusCode'] == 200
        assert json.loads(response['body']) == dict([('collection', 'some-fake-guid')])

