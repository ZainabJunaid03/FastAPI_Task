from fastapi import APIRouter, Depends
from datetime import datetime
from .database import get_db 

tasks_db = {}

tasks_router = APIRouter()

@tasks_router.post("/create")
def create_task(task_name: str, user: str = Depends(get_db)):
    current_time = datetime.utcnow()
    task = {"task_name": task_name, "created_at": current_time}
    tasks_db.setdefault(user, []).append(task)
    return {"message": "Task created successfully", "task": task}

@tasks_router.get("/list")
def list_tasks(user: str = Depends(get_db)):
    return {"tasks": tasks_db.get(user, [])}
