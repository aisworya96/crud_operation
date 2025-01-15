from flask import Flask, jsonify, request

app = Flask(__name__)

items = []


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/items', methods = ['POST'])
def create_item():
    data = request.get_json()
    item = {
        'id': len(items) + 1,
        'name': data.get('name')

    }
    items.append(item)
    return jsonify(item), 201


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    item['name'] = data.get('name', item['name'])
    return jsonify(item), 200


if __name__ == '__main__':
    app.run()