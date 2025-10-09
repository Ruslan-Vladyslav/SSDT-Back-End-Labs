from app import create_app, db
from app.models import User, Category, Record

app = create_app()

with app.app_context():
    print("Columns in User table:")
    for column in User.__table__.columns:
        print(column.name, column.type)

    print("\nColumns in Categories table:")
    for column in Category.__table__.columns:
        print(column.name, column.type)

    print("\nColumns in Record table:")
    for column in Record.__table__.columns:
        print(column.name, column.type)
