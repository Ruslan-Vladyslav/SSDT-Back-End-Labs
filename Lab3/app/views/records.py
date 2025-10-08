from flask import Blueprint, request, jsonify
from app import db
from app.models import Record, Category, User
from app.schemas import RecordSchema
from datetime import datetime

record_bp = Blueprint('record', __name__)

record_schema = RecordSchema()
records_schema = RecordSchema(many=True)


@record_bp.route('/record', methods=['POST'])
def create_record():
    json_data = request.get_json()
    errors = record_schema.validate(json_data)
    if errors:
        return jsonify(errors), 400

    record = Record(
        user_id=json_data['user_id'],
        category_id=json_data['category_id'],
        amount=json_data['amount'],
        created_at=datetime.utcnow()
    )
    db.session.add(record)
    db.session.commit()
    return jsonify(record_schema.dump(record)), 201


@record_bp.route('/record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = Record.query.get(record_id)

    if not record:
        return jsonify({"error": "Record not found"}), 404
    
    return jsonify(record_schema.dump(record)), 200


@record_bp.route('/record/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    record = Record.query.get(record_id)

    if not record:
        return jsonify({"error": "Record not found"}), 404
    
    db.session.delete(record)
    db.session.commit()

    return '', 204


@record_bp.route('/record', methods=['GET'])
def get_records():
    user_id = request.args.get('user_id', type=int)
    category_id = request.args.get('category_id', type=int)

    if user_id is not None:
        user = db.session.execute(
            db.select(User).filter_by(id=user_id)
        ).scalar_one_or_none()
        if not user:
            return jsonify({"message": f"Records for User with id {user_id} not found"}), 404

    if category_id is not None:
        category = db.session.execute(
            db.select(Category).filter_by(id=category_id)
        ).scalar_one_or_none()
        if not category:
            return jsonify({"message": f"Records with category id {category_id} not found"}), 404

    query = Record.query
    if user_id is not None:
        query = query.filter_by(user_id=user_id)
    if category_id is not None:
        query = query.filter_by(category_id=category_id)

    records = query.all()

    if not records:
        return jsonify({"message": "No records found"}), 404
    
    return jsonify(records_schema.dump(records)), 200
