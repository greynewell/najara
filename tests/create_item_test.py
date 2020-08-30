class TestCreateItem(object):
    def test_response_status_code(self, create_item):
        assert create_item['statusCode'] == 200
    def test_response_json_formatting(self, create_response_body_json):
        assert create_response_body_json['action'] == 'CREATE'
        assert create_response_body_json['target'] == 'ITEM'
        assert create_response_body_json['success'] == True
        assert isinstance(create_response_body_json['result-id'], int)
    def test_created_item_exists(self, get_created_item):
        assert get_created_item['statusCode'] == 200
    def test_created_item_values(self, created_item):
        assert created_item['name'] == 'Arrow'
        assert created_item['description'] == 'A regular wooden arrow.'
        assert created_item['type'] == 'Ammunition'
        assert created_item['quantity'] == 1
        assert created_item['weight'] == 0.05
        assert created_item['gpvalue'] == 0.05

