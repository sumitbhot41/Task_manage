from app.infrastructure.in_memory.task_repo_impl import InMemoryTaskRepository
from app.domain.services.task_service import TaskService


def test_create_task():
    repo = InMemoryTaskRepository()
    service = TaskService(repo)

    task = service.create_task(
        "Test Task",
        "Testing backend",
        1
    )

    assert task.title == "Test Task"
    assert task.is_completed is False


if __name__ == "__main__":
    test_create_task()
    print("Test passed ✅")