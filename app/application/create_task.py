class CreateTaskUseCase:

    def __init__(self, task_service):
        self.task_service = task_service

    def execute(self, data):
        return self.task_service.create_task(**data)