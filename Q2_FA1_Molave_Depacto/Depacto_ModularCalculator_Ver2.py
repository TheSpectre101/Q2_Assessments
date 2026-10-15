# Version 2: Improved modular calculator

def add_numbers(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2

def subtract_numbers(num1, num2):
    """Return the difference between two numbers."""
    return num1 - num2

def multiply_numbers(num1, num2):
    """Return the product of two numbers."""
    return num1 * num2

def divide_numbers(num1, num2):
    """Return the quotient, or None if dividing by zero."""
    if num2 == 0:
        return None
    return num1 / num2

print("Your Modular Calculator")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Choose your operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        result = add_numbers(num1, num2)
        print(f"Result: {result:g}")
    elif choice == "2":
        result = subtract_numbers(num1, num2)
        print(f"Result: {result:g}")
    elif choice == "3":
        result = multiply_numbers(num1, num2)
        print(f"Result: {result:g}")
    elif choice == "4":
        result = divide_numbers(num1, num2)
        if result is None:
            print("Cannot divide by zero.")
        else:
            print(f"Result: {result:g}")
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")

except ValueError:
    print("Invalid input. Please enter numbers only.")