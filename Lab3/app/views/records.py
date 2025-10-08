from flask import request, jsonify
from app import app
from datetime import datetime

records = {}

def records_data():
    records[1] = {"id": 1, "user_id": 2, "category_id": 2, "amount": 25.5, "created_at": datetime.now().isoformat()}
    records[2] = {"id": 2, "user_id": 3, "category_id": 3, "amount": 10.0, "created_at": datetime.now().isoformat()}

records_data()
record_counter = 3

@app.route('/record', methods=['POST'])
def create_record():
    global record_counter
    data = request.get_json()
    
    if not data or 'user_id' not in data or 'category_id' not in data or 'amount' not in data:
        return jsonify({"error": "user_id, category_id, and amount are required"}), 400

    record = {
        "id": record_counter,
        "user_id": data['user_id'],
        "category_id": data['category_id'],
        "created_at": datetime.now().isoformat(),
        "amount": data['amount']
    }

    records[record_counter] = record
    record_counter += 1
    return jsonify(record), 201


@app.route('/record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = records.get(record_id)

    if not record:
        return jsonify({"error": "Record not found"}), 404
    
    return jsonify(record), 200


@app.route('/record/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    if record_id in records:
        del records[record_id]
        return '', 204
    return jsonify({"error": "Record not found"}), 404


@app.route('/record', methods=['GET'])
def get_records():
    user_id = request.args.get('user_id', type=int)
    category_id = request.args.get('category_id', type=int)

    if user_id is None and category_id is None:
        return jsonify({"error": "Provide at least user_id or category_id"}), 400

    filtered = [
        r for r in records.values()
        if (not user_id or r['user_id'] == user_id)
        and (not category_id or r['category_id'] == category_id)
    ]
    return jsonify(filtered), 200
