from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import db
from app.models import User
from app.schemas import UserSchema

from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token

user_bp = Blueprint('user', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    all_users = User.query.all()
    if not all_users:
        return jsonify({"message": "No users found"}), 404
    return jsonify(users_schema.dump(all_users)), 200


@user_bp.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user_schema.dump(user)), 200


@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": f"User with id {user_id} has been deleted",}), 200


@user_bp.route('/register', methods=['POST'])
def register():
    json_data = request.get_json()
    errors = user_schema.validate(json_data)

    if errors:
        return jsonify(errors), 400

    if User.query.filter_by(name=json_data['name']).first():
        return jsonify({"error": "User already exists"}), 400

    new_password = pbkdf2_sha256.hash(json_data['password'])
    new_user = User(name=json_data['name'], password=new_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user)), 201


@user_bp.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()

    if not json_data.get('name') or not json_data.get('password'):
        return jsonify({"error": "Missing username or password"}), 400

    user = User.query.filter_by(name=json_data['name']).first()

    if user and pbkdf2_sha256.verify(json_data['password'], user.password):
        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token": access_token}), 200
    
    return jsonify({"error": "Invalid credentials"}), 401