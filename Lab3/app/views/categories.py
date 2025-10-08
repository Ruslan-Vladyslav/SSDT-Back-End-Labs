from flask import Blueprint, request, jsonify
from app import db
from app.models import Category
from app.schemas import CategorySchema

category_bp = Blueprint('category', __name__)

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


@category_bp.route('/categories', methods=['GET'])
def get_categories():
    user_id = request.args.get('user_id', type=int)

    if user_id is None:
        categories = Category.query.filter_by(is_custom=False).all()
    else:
        categories = Category.query.filter(
            (Category.is_custom == False) | (Category.owner_id == user_id)
        ).all()

    if not categories:
        return jsonify({"message": "No categories found"}), 404

    return jsonify(categories_schema.dump(categories)), 200


@category_bp.route('/categories', methods=['POST'])
def create_category():
    json_data = request.get_json()
    errors = category_schema.validate(json_data)
    if errors:
        return jsonify(errors), 400

    exists = Category.query.filter_by(
        name=json_data['name'],
        owner_id=json_data.get('owner_id')
    ).first()
    if exists:
        return jsonify({"error": "Category already exists"}), 400

    category = Category(
        name=json_data['name'],
        is_custom=json_data.get('owner_id') is not None,
        owner_id=json_data.get('owner_id')
    )
    
    db.session.add(category)
    db.session.commit()
    return jsonify(category_schema.dump(category)), 201


@category_bp.route('/categories/<int:cat_id>', methods=['DELETE'])
def delete_category(cat_id):
    category = Category.query.get(cat_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404

    db.session.delete(category)
    db.session.commit()

    return jsonify({"message": f"Category with id {cat_id} has been deleted",}), 200
