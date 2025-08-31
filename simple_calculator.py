# Writing functions for all operations

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "error, division by zero"
    return x/y

def power(x,y):
    return x**y

def mod(x,y):
    return x % y

def square(x):
    return x*x

def cube(x):
    return x*x*x

def square_root(x):
    if x < 0:
        return "error, square root of negative number"
    return x**0.5

def cube_root(x):
    if x < 0:
        return -(-x)**(1/3)
    return x**(1/3)

def factorial(x):
    if x < 0:
        return "error, factorial of negative number"
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def percentage(x, y):
    return (x / y) * 100

# Displaying the menu

def display_menu():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Square")
    print("8. Cube")
    print("9. Square Root")
    print("10. Cube Root")
    print("11. Factorial")
    print("12. Percentage")
    print("13. Exit")

# Main function to run the calculator

def main():
    while True:
        display_menu()
        choice = input("Enter choice (1-13): ")

        if choice == '13':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6', '12']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '6':
                print(f"{num1} % {num2} = {mod(num1, num2)}")
            elif choice == '12':
                print(f"{num1} is {percentage(num1, num2)}% of {num2}")

        elif choice in ['7', '8', '9', '10', '11']:
            num = float(input("Enter number: "))

            if choice == '7':
                print(f"Square of {num} = {square(num)}")
            elif choice == '8':
                print(f"Cube of {num} = {cube(num)}")
            elif choice == '9':
                print(f"Square root of {num} = {square_root(num)}")
            elif choice == '10':
                print(f"Cube root of {num} = {cube_root(num)}")
            elif choice == '11':
                if num.is_integer():
                    print(f"Factorial of {int(num)} = {factorial(int(num))}")
                else:
                    print("Error, factorial is not defined for non-integers")

        else:
            print("Invalid input, please select a valid operation.")

main()