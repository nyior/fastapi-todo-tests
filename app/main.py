from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from .schemas import TodoTaskModel


app = FastAPI()


all_tasks: dict = {}


@app.post("/task", response_model=TodoTaskModel)
def create_task(task: TodoTaskModel):
    task_slug = task.slug

    if all_tasks.get(task_slug) is not None:
        raise HTTPException(
            detail={'message': 'Task with this slug already exists :('}, 
            status_code=400
        )

    # Ideally this should be persisted in some db
    all_tasks[task_slug] = task
    
    return task


@app.delete("/task/{task_slug}")
def remove_task(task_slug: str):
    if all_tasks.get(task_slug) is None:
        raise HTTPException(
            detail={'message': 'No task with the specified slug found :('}, 
            status_code=404
        )

    all_tasks.pop(task_slug)


@app.get("/tasks")
def tasks():
    tasks = [
        task for task in all_tasks.values()
    ]

    return tasks


@app.get("/")
def home():
    return "Welcome to our TODO application. Add /docs to the current URL to visit our docs page"