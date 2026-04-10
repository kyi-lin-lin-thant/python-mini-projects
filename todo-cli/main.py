# SET UP DATA
import os

FILE = "tasks.txt"

# LOAD TASKS
def load_tasks():
    tasks = []

    if not os.path.exists(FILE):
        open(FILE, "w").close()

    with open(FILE, "r") as f:
        for line in f:
            line = line.strip()

            if "|" in line:
                title, done = line.split("|")
                tasks.append({
                    "title": title,
                    "done": done == "True"
                })
            else:
                # old format support
                tasks.append({
                    "title": line,
                    "done": False
                })
                
    return tasks


# SAVE TASKS
def save_tasks(tasks):
    with open(FILE, "w") as f:
        for task in tasks:
            f.write(f"{task['title']}|{task['done']}\n")

tasks = load_tasks()


# UI
def show_menu():
    print("\n==============================")
    print("📝 TO DO MANAGER")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark as Done ✔")
    print("5. Clear All Tasks 🗑️")
    print("6. Exit")
    print("==============================")


# FUNCTIONS
def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Task '{title}' added!")

def view_tasks():
    if not tasks:
        print("No task yet.")
    else:
        print("\n YOUR TASKS:")
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "❌"
            print(f"{i}. {task['title']} | [{status}]")

def remove_task():
    view_tasks()
    if not tasks:
        return
    
    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"❌ Removed '{removed['title']}'")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def mark_done():
    view_tasks()
    if not tasks:
        return
    
    try:
        index = int(input("Enter task number to mark done: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            save_tasks(tasks)
            print("✔ Task marked as done!")
        else:
            print("Invalid number.")
    except:
        print("Enter a valid number.")

def clear_tasks():
    confirm = input("Are you sure to delete all tasks? (y/n): ")
    if confirm.lower() == "y":
        tasks.clear()
        save_tasks(tasks)
        print("🗑️ All tasks deleted!")


# MAIN LOOP
while True:
    show_menu()
    choice = input("Choose option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        clear_tasks()
    elif choice == "6":
        print("👋 Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")