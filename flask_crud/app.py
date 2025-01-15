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


if __name__ == '__main__':
    app.run()