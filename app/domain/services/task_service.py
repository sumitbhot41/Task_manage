from app.domain.entities.task import Task
from app.domain.repositories.task_repository import TaskRepository


class TaskService:

    def __init__(self, repo):
        self.repo = repo

    def create_task(self, title, description, user_id):
        task = Task(title, description, user_id)
        self.repo.save(task)
        return task

    def get_all_tasks(self):
        return self.repo.get_all()   # 🔥 yahi missing tha

    def complete_task(self, task_id):
        task = self.repo.get_by_id(task_id)
        if not task:
            print("Task not found")
            return
        task.complete()
        self.repo.save(task)
        return task