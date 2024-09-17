import os

TODO_FILE = "todo.txt"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            tasks = f.read().splitlines()
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        f.write("\n".join(tasks))

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def remove_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Removed task: {removed_task}")
    else:
        print(f"Task number {task_number} not found.")

def main():
    while True:
        print("\nTo-Do List")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_tasks()
        elif choice == "2":
            task = input("Enter task description: ")
            add_task(task)
        elif choice == "3":
            list_tasks()
            task_number = int(input("Enter task number to remove: "))
            remove_task(task_number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
