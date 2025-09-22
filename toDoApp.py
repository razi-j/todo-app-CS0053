tasks = []


def add_task(task):
    """Add a new task to the list."""
    tasks.append(task.strip())
    print("Task added!\n")


def show_tasks():
    """Display all current tasks."""
    if not tasks:
        print("No tasks yet.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()


def remove_task(task_number):
    """Remove a task by its number (1-based)."""
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Removed: {removed}\n")
    else:
        print("Invalid task number.\n")


def main():
    """Main menu loop."""
    while True:
        print("------ To-Do App ------")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter choice: ").strip()
        try:
            choice = int(choice)
            if choice == 1:
                t = input("Enter task: ").strip()
                if t:
                    add_task(t)
                else:
                    print("Task cannot be empty.\n")
            elif choice == 2:
                show_tasks()
            elif choice == 3:
                if not tasks:
                    print("No tasks to remove.\n")
                    continue
                try:
                    n = int(input("Enter task number to remove: "))
                    d = str(input("Are you sure you want to remove task number " + str(n) + ". " + str(tasks[n-1]) + "? (y/n): "))
                    remove_task(n) if d.lower() == "y" else print()
                except ValueError:
                    print("Please enter a valid number.\n")
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1-4.\n")

        except ValueError:
            print("Invalid Input!\n")


if __name__ == "__main__":
    main()
