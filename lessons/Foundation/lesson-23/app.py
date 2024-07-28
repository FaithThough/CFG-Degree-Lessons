import flask
from flask import Flask, jsonify, request # Import necessary Flask functions and JSON handling
import json # Import JSON library for handling JSON data

# Creates an instance of the Flask class
app = Flask(__name__)
# Define a route for the root URL ("/")
@app.route('/') # The route decorator binds a function to a URL
def hello_world(): # Function to handle requests to the root URL
    return 'Hello world!'  # Return a simple response

# Function to read data from a JSON file
def read_data():
    with open('data.json', 'r') as file: # Open the data.json file in read mode
        return json.load(file)  # Load and return the JSON data from the file

# Define a route to get all items
# Methods: get, post, put delete -> CRUD (create, read, update, delete)
@app.route('/items', methods=['GET']) # The route decorator binds a function to the "/items" URL for GET requests
def get_items(): # Function to handle GET requests to "/items"
    data = read_data() # Read the data from the JSON file
    return jsonify(data) # Return the data as a JSON response

# Define a route to add a new item
@app.route('/items', methods=['POST'])  # The route decorator binds a function to the "/items" URL for POST requests
def add_items(): # Function to handle POST requests to "/items"
    data = read_data() # Read the data from the JSON file
    new_item = request.get_json() # Get the new item data from the request
    new_item['id'] = len(data) + 1 # Assign a new ID to the new item
    data.append(new_item) # Add the new item to the data list
    with open('data.json', 'w') as file:  # Open the data.json file in write mode
        json.dump(data, file)  # Write the updated data back to the file
    return jsonify(data), 201  # Return the updated data and a 201 Created status

# Define a route to delete an item by ID
# Define a route to delete an item by its ID
@app.route('/items/<int:item_id>', methods=['DELETE'])  # The route decorator binds the delete_item function to the "/items/<item_id>" URL for DELETE requests
def delete_item(item_id):  # Function to handle DELETE requests to "/items/<item_id>"
    data = read_data()  # Read the data from the JSON file
    item = None  # Initialize the item variable to None
    # Start searching for the item by its ID
    for d in data:  # Loop through each item in the data list
        if d['id'] == item_id:  # Check if the item's ID matches the requested ID
            item = d  # If a match is found, assign the item to the variable
            data.remove(d)  # Remove the item from the data list
            break  # Exit the loop after finding the item

    # Check if the variable 'item' is None
    if item is None:
        # If 'item' is None, it means the item was not found
        # Use the jsonify function to create a JSON response with an error message
        # The response contains a dictionary with an "error" key and the message "Item not found"
        # Also, set the HTTP status code to 404 to indicate that the item was not found
        return jsonify({"error": "Item not found"}), 404

    with open('data.json', 'w') as file:
        json.dump(data, file)  # Write the updated data back to the file

    return jsonify(item), 200  # Return the deleted item as a confirmation


if __name__ == '__main__':
    app.run(debug=True)

