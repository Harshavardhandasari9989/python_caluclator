def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b
def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    while True:
        try:
            choice = input("\nEnter your choice (1/2/3/4/5): ")
            if choice == '5':
                print("The math is done, but the knowledge continues. Until we meet again for more equations,Good Bye!")
                break
            if choice not in ['1', '2', '3', '4']:
                print("Invalid input! Please choose a valid option.")
                continue
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
calculator()
