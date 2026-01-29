FROM python:3.11-slim

# Set directory
WORKDIR /app

# Install system dependencies for both FastAPI and Npm (Serve server)
RUN apt-get update && apt-get install -y \
    sqlite3 \
    libsqlite3-dev    

# Install fastapi libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Fastapi app and entrypoint script
COPY app ./app

# EXPOSE 8000 port
EXPOSE 8000

# Execute script for multi entrypoint
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload