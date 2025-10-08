from app import app, db
from sqlalchemy import text

with app.app_context():
    try:
        result = db.session.execute(text("SELECT 1"))
        print("Database is working!")
    except Exception as e:
        print("Database connection failed:", e)
