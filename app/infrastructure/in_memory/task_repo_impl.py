from app.domain.repositories.task_repository import TaskRepository
from app.domain.entities.task import Task


class InMemoryTaskRepository(TaskRepository):

    def __init__(self):
        self.tasks = []
        self.counter = 1

    def save(self, task: Task) -> Task:
        if task.id is None:
            task.id = self.counter
            self.counter += 1
            self.tasks.append(task)
        return task

    def get_by_id(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise Exception("Task not found")

    def get_all(self):
        return self.tasks