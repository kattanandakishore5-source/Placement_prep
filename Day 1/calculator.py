try:
    number_1 = int(input("Enter first number:\n"))
    operator = input("Enter operator:\n")
    number_2 = int(input("Enter second number:\n"))

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
      
    