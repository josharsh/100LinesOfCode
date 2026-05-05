import json
import os
from datetime import datetime

FILE = "data.json"

# Initialize storage
def init():
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump({"tasks": [], "notes": []}, f)

# Load data
def load():
    with open(FILE, "r") as f:
        return json.load(f)

# Save data
def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add task
def add_task():
    title = input("Task title: ")
    data = load()
    task = {
        "title": title,
        "done": False,
        "created": str(datetime.now())
    }
    data["tasks"].append(task)
    save(data)
    print("✅ Task added!")

# View tasks
def view_tasks():
    data = load()
    tasks = data["tasks"]
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i+1}. [{status}] {t['title']}")

# Complete task
def complete_task():
    view_tasks()
    try:
        index = int(input("Task number: ")) - 1
        data = load()
        data["tasks"][index]["done"] = True
        save(data)
        print("🎉 Task completed!")
    except:
        print("Invalid input")

# Delete task
def delete_task():
    view_tasks()
    try:
        index = int(input("Task number: ")) - 1
        data = load()
        removed = data["tasks"].pop(index)
        save(data)
        print(f"🗑 Deleted: {removed['title']}")
    except:
        print("Invalid input")

# Add note
def add_note():
    text = input("Write note: ")
    data = load()
    note = {
        "text": text,
        "time": str(datetime.now())
    }
    data["notes"].append(note)
    save(data)
    print("📝 Note saved!")

# View notes
def view_notes():
    data = load()
    notes = data["notes"]
    if not notes:
        print("No notes yet.")
        return
    for i, n in enumerate(notes):
        print(f"{i+1}. {n['text']} ({n['time']})")

# Simple AI suggestion (rule-based)
def suggest():
    data = load()
    pending = [t for t in data["tasks"] if not t["done"]]
    if len(pending) > 5:
        print("⚠ You have many pending tasks. Focus on top 3.")
    elif len(pending) == 0:
        print("🎉 You're all caught up!")
    else:
        print(f"👍 {len(pending)} tasks pending. Keep going!")

# Menu
def menu():
    print("\n=== AI CLI Assistant ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Add Note")
    print("6. View Notes")
    print("7. AI Suggestion")
    print("0. Exit")

def main():
    init()
    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            add_note()
        elif choice == "6":
            view_notes()
        elif choice == "7":
            suggest()
        elif choice == "0":
            print("Goodbye 👋")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
