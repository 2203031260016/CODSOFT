
# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

print("Welcome to the Simple Calculator!")

# Input first number
num1 = float(input("Enter the first number: "))

# Input second number
num2 = float(input("Enter the second number: "))

print("Operations:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Input operation choice
choice = input("Enter operation (1/2/3/4): ")

if choice == '1':
    print("Result: ", add(num1, num2))
elif choice == '2':
    print("Result: ", subtract(num1, num2))
elif choice == '3':
    print("Result: ", multiply(num1, num2))
elif choice == '4':
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        print("Result: ", divide(num1, num2))
else:
    print("Invalid input. Please choose a valid operation.")
