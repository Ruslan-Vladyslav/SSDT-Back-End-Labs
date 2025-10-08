# Lab3 - REST API & ORM

## Local Setup
1. Navigate to the project folder

2. Create a virtual environment (optional)
```bash
python3 -m venv env
```

3. Activate the virtual environment

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Run the Flask application
```bash
flask --app app run -h 0.0.0.0 -p 8080
```

6. Test the endpoints in Postman App / locally


## Docker Setup (optional)

1. Build the Docker image
```bash
docker build . -t lab1-flask:latest
```

2. Run the container
```bash
docker run -it --rm -e PORT=8080 -p 8080:8080 lab1-flask:latest
```

3. Test the endpoints