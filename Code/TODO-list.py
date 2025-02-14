# Simple To-Do List App

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f'Task "{task}" added!')

def remove_task():
    show_tasks()
    try:
        index = int(input("Enter task number to remove: ")) - 1
        removed = tasks.pop(index)
        print(f'Task "{removed}" removed!')
    except (IndexError, ValueError):
        print("Invalid selection!")

def main():
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
