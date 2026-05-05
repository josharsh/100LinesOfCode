import os
import webbrowser
import datetime


def parse_command(command):
    command = command.lower().strip()

    if "time" in command:
        return ("time", None)

    elif "date" in command:
        return ("date", None)

    elif command.startswith("open "):
        return ("open", command.replace("open ", "").strip())

    elif command.startswith("create file "):
        return ("create", command.replace("create file ", "").strip())

    elif command.startswith("delete file "):
        return ("delete", command.replace("delete file ", "").strip())

    elif command.startswith("search "):
        return ("search", command.replace("search ", "").strip())

    elif command.startswith("calc "):
        return ("calc", command.replace("calc ", "").strip())

    elif command == "help":
        return ("help", None)

    elif "exit" in command or "quit" in command:
        return ("exit", None)

    return ("unknown", command)


def execute(action, value):
    if action == "time":
        print("🕒", datetime.datetime.now().strftime("%H:%M:%S"))

    elif action == "date":
        print("📅", datetime.date.today())

    elif action == "open":
        try:
            print(f"🌐 Opening {value}...")
            webbrowser.open(f"https://{value}.com")
        except:
            print("❌ Failed to open.")

    elif action == "create":
        try:
            with open(value, "w") as f:
                f.write("Created by AI Terminal Assistant\n")
            print(f"📄 File '{value}' created.")
        except:
            print("❌ Error creating file.")

    elif action == "delete":
        if os.path.exists(value):
            os.remove(value)
            print(f"🗑️ File '{value}' deleted.")
        else:
            print("❌ File not found.")

    elif action == "search":
        print(f"🔍 Searching: {value}")
        webbrowser.open(f"https://www.google.com/search?q={value}")

    elif action == "calc":
        try:
            result = eval(value)
            print(f"🧮 Result: {result}")
        except:
            print("❌ Invalid calculation.")

    elif action == "help":
        print("""
Commands:
- open <site>
- create file <name>
- delete file <name>
- search <query>
- calc <expression>
- time / date
- help
- exit
""")

    elif action == "exit":
        print("👋 Exiting...")
        exit()

    else:
        print("🤖 Command not recognized. Type 'help'.")


def main():
    print("🚀 AI Terminal Assistant")
    print("Type 'help' to see commands.\n")

    while True:
        user_input = input("💬 > ")
        action, value = parse_command(user_input)
        execute(action, value)


if __name__ == "__main__":
    main()
