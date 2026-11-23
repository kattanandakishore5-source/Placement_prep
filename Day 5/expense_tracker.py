import csv
import os

expenses = []

def add_expense():
    expense_name = input("Enter the name of the expense:\n").strip()
    if not expense_name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter how much amount was spent:\n"))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Value must be numeric.")
        return

    category = input("Enter the category of the expense:\n").strip()
    if not category:
        print("Category cannot be empty.")
        return

    expense = {
        "name": expense_name,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    print(f"Added '{expense_name}' ({amount}) under '{category}'.")

def display_expenses():
    if not expenses:
        print("No expenses recorded")
        return
    
    for expense in expenses:
        print(f"Name: {expense['name']}")
        print(f"Amount: ₹{expense['amount']:.2f}")
        print(f"Category: {expense['category']}")
        print()

def calculate_total():
    if not expenses:
        print("No expenses recorded")
        return
    
    total = sum(expense["amount"] for expense in expenses)

    print("========== TOTAL EXPENDITURE ==========")
    print(f"Total expenses : {total:.2f}")

def save_expenses():
    if not expenses:
        print("No expenses to save.")
        return
    try:
        with open("expenses.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["name", "amount", "category"]
            )
            writer.writeheader()
            writer.writerows(expenses)
        print("Data saved successfully.")
    except OSError as e:
        print(f"Error saving file: {e}")

def load_expenses():
    if not os.path.exists("expenses.csv"):
        print("No existing data found. Starting fresh.")
        return

    try:
        loaded_data = []
        with open("expenses.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                loaded_data.append({
                    "name": row["name"],
                    "amount": float(row["amount"]),
                    "category": row["category"]
                })

        expenses.clear()
        expenses.extend(loaded_data)
        print("Expenses loaded successfully.")
    except (OSError, KeyError, ValueError, csv.Error) as e:
        print(f"Error loading file: {e}")

def main():
    load_expenses()

    while True:
        print("\n======= EXPENSE TRACKER =======")
        print("1. Add Expense ")
        print("2. Display expense")
        print("3. Calculate total")
        print("4. Save expenses")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice:\n"))
        except ValueError:
            print("Please enter a valid choice")
            continue

        if choice == 1:
            add_expense()

        elif choice == 2:
            display_expenses()

        elif choice == 3:
            calculate_total()

        elif choice == 4:
            save_expenses()

        elif choice == 5:
            save_expenses()
            print("Exiting Expense tracker")
            break

        else:
            print("Invalid choice. Select between 1 and 5. ")

if __name__ == "__main__":
    main()