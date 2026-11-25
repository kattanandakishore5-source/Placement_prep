# Day 5: Expense Tracker

## Project Description
A personal finance command-line utility built in Python to log, categorize, and track daily expenditures. It allows users to record spending with custom categories, review logged items, calculate aggregate spending, and persist entries in a structured comma-separated values (`expenses.csv`) file using Python's standard `csv` module.

---

## Features
- **Add Expense**: Records expense title, non-negative monetary amount, and category tag.
- **Display Expenses**: Formats and lists all recorded transactions with item name, formatted currency, and category.
- **Calculate Total**: Sums all logged expenditures to provide an instant overview of total financial outflow.
- **CSV Data Persistence**: Stores records in standard `expenses.csv` with automated loading on startup and saving on shutdown.
- **Defensive Input Handling**: Catches invalid non-numeric inputs and zero/negative amounts.

---

## Python Concepts Demonstrated
- **CSV Handling**: File streaming using `csv.DictReader` for parsing rows into dictionaries and `csv.DictWriter` with `writeheader()` and `writerows()` for persistence.
- **List of Dictionaries**: In-memory modeling of tabular data (`list[dict[str, Any]]`).
- **Data Validation & Formatting**: String trimming, positive float validation, and 2-decimal place currency formatting (`{amount:.2f}`).
- **Interactive CLI Loop**: Standard procedural loop pattern with numerical selection and error recovery.
- **Path Resolution**: Relative directory resolution via `os.path.dirname(os.path.abspath(__file__))`.

---

## Requirements
- Python 3.8 or higher.
- Standard Library only (`csv`, `os` — no external packages required).

---

## How to Execute the Program

### From the Repository Root
```bash
python "Day 5/expense_tracker.py"
```

### From the `Day 5` Directory
```bash
cd "Day 5"
python expense_tracker.py
```

---

## Example Usage

### 1. View Recorded Expenses (Option 2)
```text
======= EXPENSE TRACKER =======
1. Add Expense
2. Display Expenses
3. Calculate Total
4. Save Expenses
5. Exit
Enter your choice: 2

------ Recorded Expenses ------
Name: Food
Amount: Rs. 150.00
Category: Dining

Name: Petrol
Amount: Rs. 200.00
Category: Transportation

Name: Books
Amount: Rs. 450.00
Category: Education

Name: Internet
Amount: Rs. 799.00
Category: Utilities
```

### 2. Compute Total Expenditure (Option 3)
```text
Enter your choice: 3
========== TOTAL EXPENDITURE ==========
Total expenses : Rs. 1599.00
```

### 3. Add an Expense (Option 1)
```text
Enter your choice: 1
Enter the name of the expense:
Groceries
Enter how much amount was spent:
350.50
Enter the category of the expense:
Household
Added 'Groceries' (350.50) under 'Household'.
```
