def add_task(tasks, task_name):
    """Adds a new task to the list."""
    tasks.append({"task": task_name, "done": False})
    print(f"Task '{task_name}' added.")

def view_tasks(tasks):
    """Displays all tasks with their status."""
    if not tasks:
        print("No tasks in the list.")
        return

    print("\n--- To-Do List ---")
    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index + 1}. {task['task']} - {status}")
    print("------------------")

def mark_task_done(tasks, task_index):
    """Marks a task as done based on its index."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        print(f"Task '{tasks[task_index]['task']}' marked as done.")
    else:
        print("Invalid task number.")

def delete_task(tasks, task_index):
    """Deletes a task based on its index."""
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['task']}' deleted.")
    else:
        print("Invalid task number.")
def main():
    tasks = []
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_name = input("Enter the task: ")
            add_task(tasks, task_name)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            try:
                task_num = int(input("Enter the task number to mark as done: "))
                mark_task_done(tasks, task_num - 1)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                task_num = int(input("Enter the task number to delete: "))
                delete_task(tasks, task_num - 1)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
