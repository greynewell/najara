import json, pytest

@pytest.fixture
def response_body_json(create_collection):
    return json.loads(create_collection['body'])

@pytest.fixture
def get_created_collection(response_body_json, gateway_factory):
    gateway = gateway_factory()
    collectionID = response_body_json['result-id']
    response = gateway.handle_request(method='GET',
                                        path='/collection/' + collectionID,
                                        headers={},
                                        body='')
    return response

@pytest.fixture
def created_collection(get_created_collection):
    return json.loads(get_created_collection['body'])['collection']

class TestCreateCollection(object):
    def test_response_status_code(self, create_collection):
        assert create_collection['statusCode'] == 200
    def test_response_json_formatting(self, response_body_json):
        assert response_body_json['action'] == 'CREATE'
        assert response_body_json['target'] == 'COLLECTION'
        assert response_body_json['success'] == True
        assert len(response_body_json['result-id'].split('-')) == 5
    def test_created_collection_exists(self, get_created_collection):
        assert get_created_collection['statusCode'] == 200
    def test_created_collection_values(self, created_collection):
        assert created_collection['name'] == 'test'
        assert created_collection['description'] == 'testy'

