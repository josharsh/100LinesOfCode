import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter priority (low/medium/high): ").lower()

    if priority not in ["low", "medium", "high"]:
        print("⚠ Invalid priority! Defaulting to 'low'")
        priority = "low"

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(task)
    print("✅ Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks available.")
        return

    print("\n📋 Your Tasks:\n")
    for task in tasks:
        status = "✔" if task["completed"] else "✘"
        print(f'{task["id"]}. {task["title"]} | {task["priority"].upper()} | {status}')


def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("\nEnter task ID to mark as complete: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print("🎉 Task marked as completed!")
                return
        print("❌ Task not found.")
    except ValueError:
        print("⚠ Invalid input.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("\nEnter task ID to delete: "))
        new_tasks = [task for task in tasks if task["id"] != task_id]

        if len(new_tasks) == len(tasks):
            print("❌ Task not found.")
        else:
            tasks[:] = new_tasks
            print("🗑 Task deleted successfully!")

    except ValueError:
        print("⚠ Invalid input.")


def sort_tasks(tasks):
    priority_order = {"high": 1, "medium": 2, "low": 3}
    tasks.sort(key=lambda x: priority_order.get(x["priority"], 3))
    print("🔃 Tasks sorted by priority!")


def search_tasks(tasks):
    keyword = input("🔍 Enter keyword to search: ").lower()
    results = [t for t in tasks if keyword in t["title"].lower()]

    if not results:
        print("❌ No matching tasks found.")
        return

    print("\n🔎 Search Results:\n")
    for task in results:
        print(f'{task["id"]}. {task["title"]}')


def show_stats(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed

    print("\n📊 Task Statistics:")
    print(f"Total Tasks   : {total}")
    print(f"Completed     : {completed}")
    print(f"Pending       : {pending}")


def menu():
    print("\n" + "=" * 30)
    print("🚀 SMART TASK MANAGER")
    print("=" * 30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Sort Tasks")
    print("6. Search Tasks")
    print("7. Show Stats")
    print("8. Exit")


def main():
    tasks = load_tasks()

    while True:
        menu()
        choice = input("\nChoose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            sort_tasks(tasks)
        elif choice == "6":
            search_tasks(tasks)
        elif choice == "7":
            show_stats(tasks)
        elif choice == "8":
            save_tasks(tasks)
            print("👋 Goodbye! Stay productive!")
            break
        else:
            print("⚠ Invalid choice, try again.")

        save_tasks(tasks)


if __name__ == "__main__":
    main()
