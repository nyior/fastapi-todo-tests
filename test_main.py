from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)



def test_create_task_with_valid_input():
    task = {
        "slug": "test-task", 
        "title": "Test task", 
        "description": "Just some test task",
        "status": "In progress"
    }
    response = client.post("/task", json=task)
    data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert 'title' in data and data['title'] == "Test task"


def test_create_task_with_invalid_input():
    task = {
        "slug": "test-task", 
        "title": "Test task", 
        "description": "Just some test task",
        "status": "In progress"
    }
    response = \
    client.post("/task", json=task)
    data = response.json()

    assert response.status_code != status.HTTP_200_OK
    assert 'title' not in data


def test_get_tasks_returns_data():
    response = \
    client.get("/tasks")
    data = response.json()

    assert len(data) > 0