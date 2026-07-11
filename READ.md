# FlyRank AI Backend Assignment

## Overview

This project is a simple backend API built using FastAPI.

The purpose of this assignment is to demonstrate the request-response cycle of a backend server.

## Technologies Used

- Python
- FastAPI
- Uvicorn

## API Endpoints

### GET /

Returns a welcome message.

Response:

{
    "message": "Hello from FlyRank AI Backend"
}


### GET /health

Checks if the server is running.

Response:

{
    "status": "healthy"
}

## Running Locally

Install dependencies:

pip install -r requirements.txt


Start the server:

uvicorn main:app --reload


## Testing

Browser:

http://127.0.0.1:8000

http://127.0.0.1:8000/health


Using curl:

curl http://127.0.0.1:8000

curl http://127.0.0.1:8000/health