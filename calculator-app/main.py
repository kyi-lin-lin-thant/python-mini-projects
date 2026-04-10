# ===============================
# SMART CLI CALCULATOR
# ===============================

# --------- HISTORY ---------
history = []


# --------- FUNCTIONS ---------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def show_menu():
    print("\n==============================")
    print("   🧮 PYTHON CALCULATOR")
    print("==============================")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Exit")
    print("==============================")


def get_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except:
        print("❌ Invalid input! Please enter numbers.")
    return None, None


def save_history(record):
    history.append(record)


def show_history():
    print("\n📜 CALCULATION HISTORY")
    if not history:
        print("No history yet.")
    else:
        for item in history:
            print(item)


# --------- MAIN LOOP ---------
while True:
    show_menu()
    choice = input("Choose option: ")

    if choice == "6":
        print("\n👋 Goodbye Juri!")
        break

    elif choice == "5":
        show_history()
        continue

    elif choice not in ["1", "2", "3", "4"]:
        print("❌ Invalid choice. Try again.")
        continue

    a, b = get_numbers()
    if a is None:
        continue

    if choice == "1":
        result = add(a, b)
        record = f"{a} + {b} = {result}"

    elif choice == "2":
        result = subtract(a, b)
        record = f"{a} - {b} = {result}"

    elif choice == "3":
        result = multiply(a, b)
        record = f"{a} * {b} = {result}"

    elif choice == "4":
        result = divide(a, b)
        record = f"{a} / {b} = {result}"

    print("\n✅ Result: ", result)
    save_history(record)