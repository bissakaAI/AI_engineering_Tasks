# Simple Calculator Program

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract second number from first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide first number by second
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Function to calculate square root (simple integer check)
def sqr_rt(a):
    if a <= 2 and a >= 0:
        return a
    elif a > 2:
        for x in range(3, a + 1):
            if x * x == a:
                return x
        return "Not a perfect square"
    else:
        return "Complex number"

# Function for exponentiation
def expone_ntial(a, b):
    return a ** b


print("=" * 40)
print("       SIMPLE CALCULATOR PROGRAM")
print("=" * 40)
print("Operations:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square Root")
print("6. Exponential Operation")
print("Press 'c' to clear/exit")
print("=" * 40)

while True:
    choice = input("\nEnter choice (1/2/3/4/5/6 or c): ")

    if choice.lower() == "c":
        print("\n🧹 Clearing memory... Exiting program.")
        break

    # Square root takes only one number
    if choice == '5':
        num = int(input("Enter number: "))
        result = sqr_rt(num)
        print(f"✔ Result of √{num} = {result}")
        continue

    # Other operations need two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"✔ Result of {num1} + {num2} = {result:.2f}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"✔ Result of {num1} - {num2} = {result:.2f}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"✔ Result of {num1} × {num2} = {result:.2f}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"✔ Result of {num1} ÷ {num2} = {result}")
    elif choice == '6':
        result = expone_ntial(num1, num2)
        print(f"✔ Result of {num1}^{num2} = {result:.2f}")
    else:
        print("⚠ Invalid choice, please try again!")
