class Task:
    def __init__(self, title: str, description: str, user_id: int):
        self.id = None
        self.title = title
        self.description = description
        self.user_id = user_id
        self.is_completed = False

    def complete(self):
        """Business rule to mark task complete"""
        self.is_completed = True
