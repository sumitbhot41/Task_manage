from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.task import Task


class TaskRepository(ABC):

    @abstractmethod
    def save(self, task: Task) -> Task:
        pass

    @abstractmethod
    def get_by_id(self, task_id: int) -> Task:
        pass

    @abstractmethod
    def get_all(self) -> List[Task]:
        pass