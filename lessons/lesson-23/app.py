import flask
from flask import Flask, jsonify, request
import json

app = Flask(__name__)
@app.route('/') # decorator
def hello_world():
    return 'Hello world!'

def read_data():
    with open('data.json', 'r') as file:
        return json.load(file)

# Methods: get, post, put delete -> CRUD (create, read, update, delete)
@app.route('/items', methods=['GET'])
def get_items():
    data = read_data()
    return jsonify(data)

@app.route('/items', methods=['POST'])
def add_items():
    data = read_data()
    new_item = request.get_json()
    new_item['id'] = len(data) + 1
    data.append(new_item)
    with open('data.json', 'w') as file:
        json.dump(data, file)
    return jsonify(data), 201


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    data = read_data()
    item = None
    for d in data:
        if d['id'] == item_id:
            item = d
            data.remove(d)  # Remove the item from the data list
            break

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    with open('data.json', 'w') as file:
        json.dump(data, file)  # Write the updated data back to the file

    return jsonify(item), 200  # Return the deleted item as a confirmation


if __name__ == '__main__':
    app.run(debug=True)

