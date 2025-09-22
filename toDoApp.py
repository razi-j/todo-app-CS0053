tasks = []


def add_task(task):
    tasks.append(task.strip())
    print("task added!")


def show_tasks():
    if not tasks:
        print("no tasks yet")
    else:
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])


def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("task removed!!")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        ch = input("enter choice : ").strip()
        if ch == "1":
            t = input("enter task : ").strip()
            add_task(t)
        elif ch == "2":
            show_tasks()
        elif ch == "3":
            if not tasks:
                print("No tasks to remove.")
                continue
            try:
                n = int(input("enter task no to remove: "))
                remove_task(n)
            except ValueError:
                print("Please enter a valid number.")
        elif ch == "4":
            break
        else:
            print("wrong choice!!")


if __name__ == "__main__":
    main()
