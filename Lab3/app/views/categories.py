from flask import request, jsonify
from app import app, db
from app.models import Category
from app.schemas import CategorySchema

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

# GET: загальні + користувацькі даного user_id
@app.route('/category', methods=['GET'])
def get_categories():
    user_id = request.args.get('user_id', type=int)
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    categories = Category.query.filter(
        (Category.is_custom == False) | (Category.owner_id == user_id)
    ).all()
    return categories_schema.jsonify(categories), 200

@app.route('/category', methods=['POST'])
def create_category():
    json_data = request.get_json()
    errors = category_schema.validate(json_data)
    if errors:
        return jsonify(errors), 400

    exists = Category.query.filter(
        (Category.name == json_data['name']) & 
        ((Category.is_custom == False) | (Category.owner_id == json_data.get('owner_id')))
    ).first()
    if exists:
        return jsonify({"error": "Category already exists"}), 400

    category = Category(
        name=json_data['name'],
        is_custom=bool(json_data.get('owner_id')),
        owner_id=json_data.get('owner_id')
    )
    db.session.add(category)
    db.session.commit()
    return category_schema.jsonify(category), 201

@app.route('/category/<int:cat_id>', methods=['DELETE'])
def delete_category(cat_id):
    category = Category.query.get(cat_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404

    db.session.delete(category)
    db.session.commit()
    return '', 204
