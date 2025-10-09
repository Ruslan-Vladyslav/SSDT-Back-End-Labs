from flask import Blueprint, jsonify
from datetime import datetime

healthcheck_bp = Blueprint('health', __name__)

@healthcheck_bp.route('/healthcheck')
def healthcheck():
    return jsonify({
        "status": "OK",
        "date": datetime.utcnow().isoformat()
    }), 200
