from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py', silent=True)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.views import users, categories, records, healthcheck
    app.register_blueprint(users.bp)
    app.register_blueprint(categories.bp)
    app.register_blueprint(records.bp)
    app.register_blueprint(healthcheck.bp)

    return app
