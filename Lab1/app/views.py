from app import app

@app.route('/healthcheck')
def healthcheck():
    return {'status': 'OK'}, 200