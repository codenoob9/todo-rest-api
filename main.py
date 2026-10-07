from fastapi import FastAPI

app = FastAPI()

tasks = [
    {
        "id": 1 ,
        "title": "get my task1 ",
        "completed": False
    },
    {
        "id": 2,
        "title":" get my task2",
        "completed": False
    }
]

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task