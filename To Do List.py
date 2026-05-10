class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter a task: ")
        self.tasks.append(task)
        print("Task added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks!")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def delete_task(self):
        if not self.tasks:
            print("No tasks!")
        else:
            self.view_tasks()
            task_number = int(input("Enter the task number to delete: ")) - 1
            if task_number < len(self.tasks):
                del self.tasks[task_number]
                print("Task deleted!")
            else:
                print("Invalid task number!")

def main():
    todo = ToDoList()
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")
        option = input("Choose an option: ")
        if option == "1":
            todo.add_task()
        elif option == "2":
            todo.view_tasks()
        elif option == "3":
            todo.delete_task()
        elif option == "4":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
