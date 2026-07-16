# FlyRank AI Backend Assignment

## Overview

This project is a Dockerized FastAPI backend connected to a PostgreSQL database.

It demonstrates a simple REST API capable of creating and retrieving items while following a clean repository structure.

## Tech Stack

- Python 3.14
- FastAPI
- PostgreSQL 16
- Docker
- Docker Compose
- Uvicorn

## Project Structure

```
.
├── repository/
├── sql/
├── database.py
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
└── README.md
```

## Running the Project

Clone the repository:

```bash
git clone https://github.com/Andile1-tech/flyrank-ai-backend-assignment.git
```

Navigate into the project:

```bash
cd flyrank-ai-backend-assignment
```

Start the application:

```bash
docker compose up --build
```

The API will be available at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

## API Endpoints

### GET /items

Returns all stored items.

### POST /items

Creates a new item.

Example request:

```json
{
  "name": "Laptop"
}
```

## Database

The application uses PostgreSQL running inside Docker.

Tables are automatically created during initialization using the SQL script inside the `sql` directory.

## Author

Andile M
