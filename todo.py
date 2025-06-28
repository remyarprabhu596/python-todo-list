tasks = []

def show_menu():
    print("\n==== To-Do List ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == '2':
        if not tasks:
            print("No tasks to show.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '3':
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to remove: "))
            if 0 < index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
