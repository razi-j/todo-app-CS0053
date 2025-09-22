tasks = []


def add_task(task):
    tasks.append(task)
    print("task added!")


def show_tasks():
    if len(tasks) == 0:
        print("no tasks yet")
    else:
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])


def remove_task(task_number):
    tasks.pop(task_number)
    print("task removed!!")


def main():
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        ch = input("enter choice : ")
        if ch == "1":
            t = input("enter task : ")
            add_task(t)
        elif ch == "2":
            show_tasks()
        elif ch == "3":
            n = int(input("enter task no to remove: "))
            remove_task(n)
        elif ch == "4":
            break
        else:
            print("wrong choice!!")


if __name__ == "__main__":
    main()
