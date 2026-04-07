import math

# --- Basic Functions ---
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# --- Advanced Functions ---
def square(x):
    return x ** 2

def exponent(x, y):
    return x ** y

def logarithm(x):
    if x <= 0:
        return "Error! Logarithm only accepts positive numbers."
    return math.log10(x) # Calculates Base-10 logarithm

print("=== Advanced Python Calculator ===")
print("Select an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
print("5. Square (x²)")
print("6. Exponent (xʸ)")
print("7. Logarithm (base 10)")

while True:
    # Take input from the user
    choice = input("\nEnter choice (1-7) or type 'q' to quit: ")

    # Check if the user wants to quit
    if choice.lower() == 'q':
        print("Closing the calculator. Goodbye!")
        break

    # Check if the choice is one of the valid options
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        try:
            # Everyone needs at least one number
            num1 = float(input("Enter the first number (or base value): "))
            
            # Only ask for a second number if the operation requires it
            if choice in ('1', '2', '3', '4', '6'):
                num2 = float(input("Enter the second number (or power): "))
        except ValueError:
            print("Invalid input! Please enter numerical values.")
            continue

        # Execute the chosen operation
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {num1} squared = {square(num1)}")
        elif choice == '6':
            print(f"Result: {num1} to the power of {num2} = {exponent(num1, num2)}")
        elif choice == '7':
            print(f"Result: log10({num1}) = {logarithm(num1)}")
            
        print("-" * 30)
    else:
        print("Invalid Input! Please select a valid operation from the menu.")
