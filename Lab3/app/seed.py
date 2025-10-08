from app import create_app, db
from app.models import User, Category, Record
from datetime import datetime

def seed_data():
    if not User.query.filter_by(name="Alice").first():
        user1 = User(name="Alice")
        db.session.add(user1)
    if not User.query.filter_by(name="Bob").first():
        user2 = User(name="Bob")
        db.session.add(user2)

    if not Category.query.filter_by(name="Food").first():
        cat1 = Category(name="Food", is_custom=False)
        db.session.add(cat1)
    if not Category.query.filter_by(name="Sweet-Food").first():
        cat2 = Category(name="Food", is_custom=True)
        db.session.add(cat2)
    if not Category.query.filter_by(name="Transport").first():
        cat3 = Category(name="Transport", is_custom=False)
        db.session.add(cat3)

    if not Record.query.first():
        rec1 = Record(user_id=1, category_id=1, amount=100, created_at=datetime.utcnow())
        rec2 = Record(user_id=2, category_id=2, amount=50, created_at=datetime.utcnow())
        db.session.add_all([rec1, rec2])

    db.session.commit()
    print("Database seeded successfully!")


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        seed_data()
