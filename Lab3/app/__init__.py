from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py', silent=False)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.views import user_bp
    app.register_blueprint(user_bp)

    from app.views import category_bp
    app.register_blueprint(category_bp)

    from app.views import record_bp
    app.register_blueprint(record_bp)

    from app.views import healthcheck_bp
    app.register_blueprint(healthcheck_bp)

    return app
