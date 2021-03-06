from chalice import Chalice
from controllers import collection, item

app = Chalice(app_name='najara')


@app.route('/')
def readCollections():
    return collection.listAll()

@app.route('/collection', methods=['POST'])
def createCollection():
    data = app.current_request.json_body
    return collection.create(data)

@app.route('/collection/{collectionGuid}', methods=['GET'])
def readCollection(collectionGuid):
    return collection.read(collectionGuid)

@app.route('/collection/{collectionGuid}', methods=['PATCH'])
def updateCollection(collectionGuid):
    data = app.current_request.json_body
    return collection.update(data, collectionGuid)

@app.route('/item/{collectionGuid}', methods=['POST'])
def createItem(collectionGuid):
    data = app.current_request.json_body
    return item.create(data, collectionGuid)

@app.route('/item/{collectionGuid}/{itemId}', methods=['GET'])
def readItem(collectionGuid, itemId):
    return item.read(itemId, collectionGuid)

@app.route('/item/{collectionGuid}/{itemId}', methods=['PUT'])
def updateItem(collectionGuid, itemId):
    data = app.current_request.json_body
    return item.update(data, itemId, collectionGuid)

@app.route('/item/{collectionGuid}/{itemId}', methods=['DELETE'])
def deleteItem(collectionGuid, itemId):
    return item.delete(itemId, collectionGuid)

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
