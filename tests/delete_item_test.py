import json, pytest

@pytest.fixture
def delete_item(gateway_factory, created_item):
    gateway = gateway_factory()
    response = gateway.handle_request(method='DELETE', path='/item/test-collection-guid-for-item/'+ str(created_item['id']),
                                    headers={'Content-Type':'application/json'},
                                    body='')
    return response

@pytest.fixture
def delete_response_body_json(delete_item):
    return json.loads(delete_item['body'])

@pytest.fixture
def get_deleted_item(delete_response_body_json, gateway_factory):
    gateway = gateway_factory()
    itemID = delete_response_body_json['result-id']
    response = gateway.handle_request(method='GET',
                                        path='/item/test-collection-guid-for-item/' + str(itemID),
                                        headers={},
                                        body='')
    return response

@pytest.fixture
def deleted_item(get_deleted_item):
    return json.loads(get_deleted_item['body'])

class TestUpdateItem(object):
    def test_response_status_code(self, delete_item):
        assert delete_item['statusCode'] == 200
    def test_response_json_formatting(self, delete_response_body_json, created_item):
        assert delete_response_body_json['action'] == 'DELETE'
        assert delete_response_body_json['target'] == 'ITEM'
        assert delete_response_body_json['success'] == True
        assert delete_response_body_json['result-id'] == created_item['id']
    def test_deleted_item_not_exists(self, get_deleted_item):
        assert get_deleted_item['statusCode'] == 404
