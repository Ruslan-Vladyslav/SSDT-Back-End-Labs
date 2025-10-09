from ..app import create_app, db
from sqlalchemy import text

app = create_app()
with app.app_context():
    try:
        db.session.execute(text("SELECT 1"))
        print("✅ Database is working!")
    except Exception as e:
        print("❌ Database connection failed:", e)
