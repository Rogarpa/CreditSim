# Python image
FROM python:3.11-slim

# Work directory
WORKDIR /app

# Python dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app ./app

# Expose port of the app
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]
