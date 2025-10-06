from flask import request, jsonify
from app import app

users = {}
user_counter = 1

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    return jsonify(user), 200

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users.pop(user_id, None)
    return '', 204

@app.route('/user', methods=['POST'])
def create_user():
    global user_counter
    data = request.get_json()
    user = {"id": user_counter, "name": data['name']}
    users[user_counter] = user
    user_counter += 1
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200