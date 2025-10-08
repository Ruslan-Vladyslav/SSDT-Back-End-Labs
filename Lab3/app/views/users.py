from flask import request, jsonify
from app import app
from app.schemas import UserSchema

users = {}
user_counter = {"value": 1}
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify(user), 200

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    users.pop(user_id)
    return '', 204

@app.route('/user', methods=['POST'])
def create_user():
    json_data = request.get_json()
    errors = user_schema.validate(json_data)
    if errors:
        return jsonify(errors), 400

    user_id = user_counter["value"]
    user = {"id": user_id, "name": json_data['name']}
    users[user_id] = user
    user_counter["value"] += 1
    return user_schema.jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
     return users_schema.jsonify(list(users.values())), 200