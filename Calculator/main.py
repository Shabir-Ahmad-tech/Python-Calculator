# Make a simple calculator using Python

import math  # import math module
def calculator():
    while True:
        print("\n___Simple Calculator___")
        operation = input("Enter operation (+, -, *, /, sqrt, ^, exit): ")  # input operation

        if operation == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        elif operation == 'sqrt':
            num = float(input("Enter number to find square root: "))
            try:
                num = math.sqrt(num)
                print(f"The square root of {num} is {num}")
            except ValueError:
                print("Error: Cannot compute square root of a negative number.")
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == '+':
                result = num1 + num2
                print(f"The result of {num1} + {num2} = {result}")

            elif operation == '-':
                result = num1 - num2
                print(f"The result of {num1} - {num2} = {result}")
            
            elif operation == '*': 
                result = num1 * num2
                print(f"The result of {num1} * {num2} = {result}")
            
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} = {result}")
            elif operation == "^":
                result = num1 ** num2
                print(f"The result of {num1} ^ {num2} = {result}")
            else:
                print("Invalid operation. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
calculator()
