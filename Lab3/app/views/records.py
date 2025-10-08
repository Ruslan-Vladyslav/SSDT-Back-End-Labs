from flask import request, jsonify
from app import app
from datetime import datetime
from app.schemas import RecordSchema

records = {}
record_counter = {"value": 1}
record_schema = RecordSchema()
records_schema = RecordSchema(many=True)

@app.route('/record', methods=['POST'])
def create_record():
    json_data = request.get_json()
    errors = record_schema.validate(json_data)
    if errors:
        return jsonify(errors), 400

    record_id = record_counter["value"]
    record = {
        "id": record_id,
        "user_id": json_data['user_id'],
        "category_id": json_data['category_id'],
        "amount": json_data['amount'],
        "created_at": datetime.now().isoformat()
    }
    records[record_id] = record
    record_counter["value"] += 1
    return record_schema.jsonify(record), 201


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

    filtered = [
        r for r in records.values()
        if (user_id is None or r['user_id'] == user_id)
        and (category_id is None or r['category_id'] == category_id)
    ]
    return records_schema.jsonify(filtered), 200