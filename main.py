from app.domain.repositories.in_memory_task_repository import InMemoryTaskRepository
#from app.application.services.task_service import TaskService
from app.domain.services.task_service import TaskService

def main():
    repo = InMemoryTaskRepository()
    service = TaskService(repo)

    while True:
        print("\n===== Task Manager =====")
        print("1. Add Task")
        print("2. Show All Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter title: ")
            description = input("Enter description: ")
            user_id = int(input("Enter user id: "))

            task = service.create_task(title, description, user_id)
            print(f"Task created with ID: {task.id}")

        elif choice == "2":
            tasks = service.get_all_tasks()

            if not tasks:
                print("No tasks found")
            else:
                for task in tasks:
                    status = "Completed" if task.is_completed else "Pending"
                    print(f"ID: {task.id} | {task.title} | {status}")

        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            service.complete_task(task_id)
            print("Task completed")

        elif choice == "4":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()