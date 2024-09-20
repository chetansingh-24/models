FROM python:3.11-slim-bullseye

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0

RUN pip install --no-cache-dir fastapi uvicorn[standard] pydantic sentence-transformers

RUN pip install --no-cache-dir fastapi[all]

EXPOSE 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
