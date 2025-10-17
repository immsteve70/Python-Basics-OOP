task_list = []

try:
    with open("tasklist.txt", "r") as file:
        for line in file:
            task_list.append(line.strip())
except FileNotFoundError:
    task_list = []

def add_task():
    action_addtask = input("Enter a new task: ")
    task_list.append(action_addtask)
    print(f"{action_addtask} has been added!")

def rem_task():
    if not task_list:
        print("No tasks to remove!")
        return
    print(task_list)
    action_remtask = input("Which task do you want to remove: ")
    if action_remtask in task_list:
        task_list.remove(action_remtask)
        print(f"{action_remtask} has been removed!")
    else:
        print("Task not found!")

def view_task():
    if not task_list:
        print("No tasks to view!")
    else:
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}\n")

def save_task():
    with open("tasklist.txt", "w") as file:
        for task in task_list:
            file.write(task + "\n")

while True:
    print("1. Add Task\n2. Remove Task\n3. View Task\n4. Exit")
    action = int(input("Choose: "))

    if action == 1:
        add_task()
    elif action == 2:
        rem_task()
    elif action == 3:
        view_task()
    elif action == 4:
        save_task()
        print("Goodbyeee!!")
        break
    else:
        continue