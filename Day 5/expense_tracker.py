"""Day 5: Command-Line Expense Tracker.

Tracks personal financial expenses with categories and amounts, computes
aggregate expenditure, and persists data to a CSV file using DictReader/DictWriter.
"""

import csv
import os

# Target the data file in the same directory as this script
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.csv")

expenses = []


def add_expense():
    """Prompt the user for expense details and append to the expense list."""
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
        "category": category,
    }
    expenses.append(expense)
    print(f"Added '{expense_name}' ({amount:.2f}) under '{category}'.")


def display_expenses():
    """Display all recorded expenses with amounts and categories."""
    if not expenses:
        print("No expenses recorded")
        return

    print("------ Recorded Expenses ------")
    for expense in expenses:
        print(f"Name: {expense['name']}")
        print(f"Amount: Rs. {expense['amount']:.2f}")
        print(f"Category: {expense['category']}")
        print()


def calculate_total():
    """Compute and display total expenditure across all recorded expenses."""
    if not expenses:
        print("No expenses recorded")
        return

    total = sum(expense["amount"] for expense in expenses)

    print("========== TOTAL EXPENDITURE ==========")
    print(f"Total expenses : Rs. {total:.2f}")


def save_expenses():
    """Persist all expense records to the CSV file."""
    if not expenses:
        print("No expenses to save.")
        return

    try:
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
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
    """Load expense records from the CSV file into memory."""
    if not os.path.exists(DATA_FILE):
        print("No existing data found. Starting fresh.")
        return

    try:
        loaded_data = []
        with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                loaded_data.append({
                    "name": row["name"],
                    "amount": float(row["amount"]),
                    "category": row["category"],
                })

        expenses.clear()
        expenses.extend(loaded_data)
        print("Expenses loaded successfully.")
    except (OSError, KeyError, ValueError, csv.Error) as e:
        print(f"Error loading file: {e}")


def main():
    """Main CLI menu loop for the Expense Tracker."""
    load_expenses()

    while True:
        print("\n======= EXPENSE TRACKER =======")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Calculate Total")
        print("4. Save Expenses")
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
            print("Invalid choice. Select between 1 and 5.")


if __name__ == "__main__":
    main()