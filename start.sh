#!/bin/bash

# Start Uvicorn in the background
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload &

# Start Serve
serve -s ./static_front -l 5000
