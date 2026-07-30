FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY docker/gunicorn.conf.py ./gunicorn.conf.py

ENV PORT=8000

CMD ["gunicorn", "-c", "gunicorn.conf.py", "src.api.main:app"]
