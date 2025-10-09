# Lab4 - REST API & ORM

## Variant

**Group Number:** `5`  
**Variant:** `5 mod 3` = 2  

- `1` → Currencies  
- `2` → Custom expense categories  
- `0` → Income tracking  

**This project implements:**  
- **Custom expense categories** (variant 2)  
  - Public categories (visible to all users)  
  - User-specific categories (visible only to the owner)

---

## Local Setup

Follow these steps to run the project locally with PostgreSQL.

1. Clone the repository and navigate to project folder

2. Create a virtual environment
```bash
python -m venv env
source env/bin/activate      # Linux/macOS
env\Scripts\activate         # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
POSTGRES_USER=user         # your user name
POSTGRES_PASSWORD=password # your password
POSTGRES_DB=db
DB_HOST=localhost
FLASK_APP=app
FLASK_ENV=development
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=8080
```

5. Run PostgreSQL locally
   - Option A — Install PostgreSQL
   - Option B — Run PostgreSQL via Docker:
    ```bash
    docker run --name expenses-db -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mysecurepassword -e POSTGRES_DB=expenses_db -p 5432:5432 -d postgres:15
    ```

    ```bash
    docker-compose build
    docker-compose up -d
    ```
     ```bash
    docker-compose down -v # delete database
    ```

    To initialize database with migrations use:
    ```bash
    flask db upgrade
    ```


6. Initialize seed data (optional)
```bash
 python -m app.seed 
```

7. Run the Flask application
```bash
 python -m app # or flask run
```