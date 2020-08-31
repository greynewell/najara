import json, pytest

new_name = "Frodo's Items"

@pytest.fixture
def update_collection_name(gateway_factory, collection, create_collection):
    collectionId = json.loads(create_collection['body'])['result-id']
    gateway = gateway_factory()
    response = gateway.handle_request(method='PATCH', path='/collection/' + str(collectionId),
                                    headers={'Content-Type':'application/json'},
                                    body='{"name":"' + new_name + '"}')
    return response

@pytest.fixture
def response_body_json(update_collection_name):
    return json.loads(update_collection_name['body'])

@pytest.fixture
def get_updated_collection(response_body_json, gateway_factory):
    gateway = gateway_factory()
    collectionID = response_body_json['result-id']
    response = gateway.handle_request(method='GET',
                                        path='/collection/' + collectionID,
                                        headers={},
                                        body='')
    return response

@pytest.fixture
def updated_collection(get_updated_collection):
    return json.loads(get_updated_collection['body'])

class TestUpdateCollection(object):
    def test_response_status_code(self, update_collection_name):
        assert update_collection_name['statusCode'] == 200
    def test_response_json_formatting(self, response_body_json):
        assert response_body_json['action'] == 'UPDATE'
        assert response_body_json['target'] == 'COLLECTION'
        assert response_body_json['success'] == True
        assert len(response_body_json['result-id'].split('-')) == 5
    def test_created_collection_values(self, updated_collection):
        assert updated_collection['collection']['name'] == new_name #should show update
        assert updated_collection['collection']['description'] == 'testy' #should remain unchanged

