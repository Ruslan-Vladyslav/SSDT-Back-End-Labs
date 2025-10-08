import os
from dotenv import load_dotenv

load_dotenv()

if os.getenv("DATABASE_URL"):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
else:
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    DB_HOST = os.getenv('DB_HOST', 'localhost')

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:5432/{POSTGRES_DB}"
    )

SQLALCHEMY_TRACK_MODIFICATIONS = False
