"""Day 1: Simple Command-Line Calculator.

Performs basic arithmetic operations (+, -, *, /) with error handling
for invalid input types and division by zero.
"""


def calculate():
    """Execute a single calculation based on user input."""
    try:
        raw_num1 = input("Enter first number:\n")
        number_1 = float(raw_num1) if "." in raw_num1 else int(raw_num1)

        operator = input("Enter operator:\n").strip()

        raw_num2 = input("Enter second number:\n")
        number_2 = float(raw_num2) if "." in raw_num2 else int(raw_num2)

        if operator == "+":
            print("Addition selected")
            result = number_1 + number_2
            print(result)

        elif operator == "-":
            print("Subtraction selected")
            result = number_1 - number_2
            print(result)

        elif operator == "*":
            print("Multiplication selected")
            result = number_1 * number_2
            print(result)

        elif operator == "/":
            print("Division selected")
            result = number_1 / number_2
            print(result)

        else:
            print("Enter a valid operator")

    except ValueError:
        print("Enter a valid number")

    except ZeroDivisionError:
        print("Can't divide a number with zero")


if __name__ == "__main__":
    calculate()

      
    