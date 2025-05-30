# match_case_calculator.py

# Prompt user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt for operation
operation = input("Choose the operation (+, -, *, /): ").strip()

# Perform the calculation using if-elif-else
if operation == "+":
    result = num1 + num2
    print(f"The result is {result}.")
elif operation == "-":
    result = num1 - num2
    print(f"The result is {result}.")
elif operation == "*":
    result = num1 * num2
    print(f"The result is {result}.")
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"The result is {result}.")
else:
    print("Invalid operation selected.")
