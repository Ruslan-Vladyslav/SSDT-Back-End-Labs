from flask import request, jsonify
from app import app

categories = {}
category_counter = 1

@app.route('/category', methods=['GET'])
def get_categories():
    return jsonify(list(categories.values())), 200

@app.route('/category', methods=['POST'])
def create_category():
    global category_counter
    data = request.get_json()

    if any(cat['name'] == data['name'] for cat in categories.values()):
        return jsonify({"error": "Category already exists"}), 400

    category = {"id": category_counter, "name": data['name']}
    categories[category_counter] = category
    category_counter += 1
    return jsonify(category), 201

@app.route('/category/<int:cat_id>', methods=['DELETE'])
def delete_category(cat_id):
    if cat_id in categories:
        del categories[cat_id]
        return '', 204