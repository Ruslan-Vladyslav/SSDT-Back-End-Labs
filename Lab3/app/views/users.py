from flask import Blueprint, jsonify, request
from app import db
from app.models import User
from app.schemas import UserSchema

user_bp = Blueprint('user', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_bp.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    if not all_users:
        return jsonify({"message": "No users found"}), 404
    return jsonify(users_schema.dump(all_users)), 200


@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user_schema.dump(user)), 200


@user_bp.route('/user', methods=['POST'])
def create_user():
    json_data = request.get_json()
    errors = user_schema.validate(json_data)
    if errors:
        return jsonify(errors), 400

    new_user = User(name=json_data['name'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user)), 201


@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return '', 204