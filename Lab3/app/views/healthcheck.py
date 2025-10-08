from app import app
from flask import jsonify
from datetime import datetime

@app.route('/healthcheck')
def healthcheck():
     return jsonify({
        "status": "OK",
        "date": datetime.utcnow().isoformat()
    }), 200