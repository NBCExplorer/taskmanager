import os
import pytest
from app.logic_layer import TaskManager

# Example fixture for initializing TaskManager with a test database configuration.
@pytest.fixture
def task_manager():
    test_config = {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME"),
    }
    manager = TaskManager(test_config)
    yield manager
    manager.close()

def test_add_task(task_manager):
    task_text = "Test task"
    task_id = task_manager.add_task(task_text)
    tasks = task_manager.load_tasks()
    assert any(task["id"] == task_id and task["task_text"] == task_text for task in tasks)
    # Cleanup: Remove the added task if needed

def test_update_task(task_manager):
    task_text = "Initial task"
    task_id = task_manager.add_task(task_text)
    new_text = "Updated task"
    task_manager.update_task(new_text, task_id)
    tasks = task_manager.load_tasks()
    assert any(task["id"] == task_id and task["task_text"] == new_text for task in tasks)

def test_delete_task(task_manager):
    task_text = "Task to be deleted"
    task_id = task_manager.add_task(task_text)
    task_manager.delete_task(task_id)
    tasks = task_manager.load_tasks()
    assert not any(task["id"] == task_id for task in tasks)