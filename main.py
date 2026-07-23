from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from repository.sqlite_repository import SQLiteRepository

app = FastAPI()

repo = SQLiteRepository()


class Task(BaseModel):
    title: str
    done: bool = False


@app.get("/")
def home():
    return {"message": "Hello from FlyRank AI Backend"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/tasks")
def get_tasks():

    rows = repo.get_tasks()

    return [
        {
            "id": row["id"],
            "title": row["title"],
            "done": bool(row["done"]),
        }
        for row in rows
    ]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    task = repo.get_task_by_id(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return {
        "id": task["id"],
        "title": task["title"],
        "done": bool(task["done"]),
    }


@app.post("/tasks", status_code=201)
def add_task(task: Task):

    repo.add_task(task.title)

    return {"message": "Task added successfully"}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):

    updated = repo.update_task(
        task_id,
        task.title,
        task.done,
    )

    if updated == 0:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return {"message": "Task updated successfully"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    deleted = repo.delete_task(task_id)

    if deleted == 0:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return {"message": "Task deleted successfully"}
