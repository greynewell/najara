import json, pytest

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
def response_body_json(create_item):
    return json.loads(create_item['body'])

@pytest.fixture
def get_created_item(response_body_json, gateway_factory):
    gateway = gateway_factory()
    itemID = response_body_json['result-id']
    response = gateway.handle_request(method='GET',
                                        path='/item/test-collection-guid-for-item/' + str(itemID),
                                        headers={},
                                        body='')
    return response

@pytest.fixture
def created_collection(get_created_collection):
    return json.loads(get_created_collection['body'])

class TestCreateCollection(object):
    def test_response_status_code(self, create_item):
        assert create_item['statusCode'] == 200
    def test_response_json_formatting(self, response_body_json):
        assert response_body_json['action'] == 'CREATE'
        assert response_body_json['target'] == 'ITEM'
        assert response_body_json['success'] == True
        assert isinstance(response_body_json['result-id'], int)
    def test_created_item_exists(self, get_created_item):
        assert get_created_item['statusCode'] == 200
    def test_created_item_values(self, created_collection):
        assert created_item['name'] == 'test'
        assert created_item['description'] == 'testy'

