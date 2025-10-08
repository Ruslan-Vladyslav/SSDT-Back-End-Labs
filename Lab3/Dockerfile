FROM python:3.11.3-slim-bullseye

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD flask --app app run -h 0.0.0.0 -p $PORT