from flask import request, jsonify
from app import app
import uuid

users = {}

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
    data = request.get_json()
    user_id = str(uuid.uuid4())
    user = {"id": user_id, "name": data['name']}
    users[user_id] = user
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200