tasks = []

def show_tasks():
    print("\n" + "-" * 30)
    print("📌 Your To-Do List 📌")
    print("-" * 30)

    if not tasks:
        print("✅ No tasks yet. Add one!\n")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")
    
    print("-" * 30)

def add_task():
    task = input("➕ Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f'✅ Task "{task}" added!')
    else:
        print("⚠️ Task cannot be empty!")

def remove_task():
    show_tasks()
    try:
        index = int(input("❌ Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f'🗑️ Task "{removed}" removed!')
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

def main():
    while True:
        print("\n" + "=" * 30)
        print("📜 To-Do List Menu 📜")
        print("=" * 30)
        print("1️⃣ View Tasks")
        print("2️⃣ Add Task")
        print("3️⃣ Remove Task")
        print("4️⃣ Exit")
        print("=" * 30)
        
        choice = input("🔹 Choose an option: ").strip()

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
