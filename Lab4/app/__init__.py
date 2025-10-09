from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager() 

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py', silent=False)

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)  

    from app.views import user_bp, category_bp, record_bp, healthcheck_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(record_bp)
    app.register_blueprint(healthcheck_bp)

    # with app.app_context():
    #     db.create_all()

    return app
