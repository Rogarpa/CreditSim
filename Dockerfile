FROM python:3.11-slim

# Set directory
WORKDIR /app

# Install system dependencies for both FastAPI and Npm (Serve server)
RUN apt-get update && apt-get install -y \
    sqlite3 \
    libsqlite3-dev    
RUN apt install -y npm
RUN npm install -g serve

# Install fastapi libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Fastapi app and entrypoint script
COPY app ./app
COPY ./start.sh /start.sh
RUN chmod +x /start.sh

# Copy front static files
COPY ./html ./static_front

EXPOSE 8000
EXPOSE 5000

# Execute script for multi entrypoint
CMD ["/start.sh"]