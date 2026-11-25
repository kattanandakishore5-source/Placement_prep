# Day 1: Command-Line Calculator & Complexity Notes

## Project Description
A command-line arithmetic calculator built in Python as part of the backend placement preparation roadmap. The tool prompts the user for two operands and an operator, computes the resulting mathematical value, and includes defensive error handling against invalid numerical inputs and zero division. It also includes comprehensive technical reference notes analyzing time and space complexity.

---

## Features
- **Standard Arithmetic Operations**: Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Flexible Numeric Support**: Handles both integers and floating-point numbers seamlessly.
- **Defensive Error Handling**:
  - Catches `ValueError` when non-numeric inputs are provided.
  - Catches `ZeroDivisionError` when attempting to divide by zero.
  - Validates operator selection and warns on unsupported symbols.
- **Asymptotic Complexity Notes**: Companion `complexity_notes.md` with Big-O analysis of elementary operations and Python built-in data structures.

---

## Python Concepts Demonstrated
- **User Input & Output**: Standard I/O using `input()` and `print()`.
- **Conditional Control Flow**: Multi-branch decision making using `if`, `elif`, and `else`.
- **Exception Handling**: Defensive programming with `try`, `except ValueError`, and `except ZeroDivisionError`.
- **Data Types & Type Casting**: Converting string inputs to `int` / `float`.
- **Modular Script Structure**: Clean function encapsulation with `if __name__ == "__main__":` entry point.

---

## Requirements
- Python 3.8 or higher.
- Standard Library only (no external third-party dependencies required).

---

## How to Execute the Program

### From the Repository Root
```bash
python "Day 1/calculator.py"
```

### From the `Day 1` Directory
```bash
cd "Day 1"
python calculator.py
```

---

## Example Usage

### 1. Successful Addition
```text
Enter first number:
15
Enter operator:
+
Enter second number:
27
Addition selected
42
```

### 2. Division with Floating-Point Result
```text
Enter first number:
10
Enter operator:
/
Enter second number:
4
Division selected
2.5
```

### 3. Error Handling - Division by Zero
```text
Enter first number:
25
Enter operator:
/
Enter second number:
0
Division selected
Can't divide a number with zero
```

### 4. Error Handling - Invalid Input
```text
Enter first number:
abc
Enter a valid number
```
