from fastapi import FastAPI
from pydantic import BaseModel

from repository.postgres_repository import PostgresRepository

app = FastAPI()

repo = PostgresRepository()


class Item(BaseModel):
    name: str


@app.get("/")
def home():
    return {"message": "Hello from FlyRank AI Backend"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/items")
def get_items():

    rows = repo.get_items()

    return [{"id": row[0], "name": row[1], "created_at": row[2]} for row in rows]


@app.post("/items")
def add_item(item: Item):

    repo.add_item(item.name)

    return {"message": "Item added successfully"}
