
class InMemoryTaskRepository:

    def __init__(self):
        self.tasks = {}
        self.counter = 1

    def save(self, task):
        if task.id is None:
            task.id = self.counter
            self.counter += 1
        self.tasks[task.id] = task

    def get_by_id(self, task_id):
        return self.tasks.get(task_id)

    # 🔥 Yaha add karo
    def get_all(self):
        return list(self.tasks.values())