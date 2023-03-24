tasks = []

while True:
    print("To-Do List Manager")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")
    
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        task = input("Enter task to add: ")
        tasks.append(task)
        print("Task added successfully.")
    elif choice == 2:
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed successfully.")
        else:
            print("Task not found in list.")
    elif choice == 3:
        if tasks:
            print("Tasks in list:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
        else:
            print("No tasks in list.")
    elif choice == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid choice, try again.")
