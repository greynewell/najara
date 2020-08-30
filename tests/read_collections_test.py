import json, pytest

@pytest.fixture
def read_collections(gateway_factory, collection, create_collection):
    gateway = gateway_factory()

    response = gateway.handle_request(method='GET', path='/',
                                    headers={'Content-Type':'application/json'},
                                    body='')
    return response

@pytest.fixture
def response_body_json(read_collections):
    return json.loads(read_collections['body'])

@pytest.fixture
def first_result(response_body_json):
    return response_body_json['collections'][0]

class TestReadCollections(object):
    def test_response_status_code(self, read_collections):
        assert read_collections['statusCode'] == 200
    def test_response_json_formatting(self, response_body_json):
        assert isinstance(response_body_json['collections'], list)
        assert len(response_body_json['collections']) >= 1
    def test_result_json_formatting(self, first_result):
        assert isinstance(first_result['id'], str)
        assert len(first_result['id'].split('-')) == 5
        assert isinstance(first_result['name'], str)
        assert isinstance(first_result['description'], str)
