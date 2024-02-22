# Math Calculator

# Function to calculate the sum of two numbers
def calculate_sum(a, b):
    return a + b

# Function to calculate the difference of two numbers
def calculate_difference(a, b):
    return a - b

# Function to calculate the product of two numbers
def calculate_product(a, b):
    return a * b

# Function to calculate the quotient of two numbers
def calculate_quotient(a, b):
    if b == 0:
        print("Error: division by zero")
        return None
    else:
        return a / b

# Function to calculate the discriminant of a quadratic equation
def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

# Function to solve a quadratic equation
def solve_quadratic(a, b, c):
    discriminant = calculate_discriminant(a, b, c)
    if discriminant < 0:
        print("Error: no real solutions")
        return None
    else:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return x1, x2

def calculate_exponentiation (base, exponent):
    return a**b

def calculate_logarithm(base, number):
    answer = manual_logarithm(number, base, 0.0001)
    return answer

def manual_logarithm(number, base):
    if number <= 0 or base <= 0 or base == 1:
        print("Error: Invalid input")
    else:
        result = 0
        while True:
            number /= base
            result += 1
            if number < base:
                break
        answer = 0
        float(answer)
        answer = (number % base)/number
        print(answer)
        # result += number/(number % base)

        return round(result, 4)

# Function to display the menu
def display_menu():
    print("Math Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Solve quadratic equation")
    print("6. Exponentiate")
    print("7. Compute Logarithm")
    print("8. Exit")

# Command-line interface
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("Result: ", calculate_sum(a, b))
        except ValueError:
            print("Error: invalid input")

    elif choice == "2":
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("Result: ", calculate_difference(a, b))
        except ValueError:
            print("Error: invalid input")

    elif choice == "3":
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("Result: ", calculate_product(a, b))
        except ValueError:
            print("Error: invalid input")

    elif choice == "4":
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = calculate_quotient(a, b)
            if result is not None:
                print("Result: ", result)
        except ValueError:
            print("Error: invalid input")

    elif choice == "5":
        try:
            a = float(input("Enter the coefficient a: "))
            b = float(input("Enter the coefficient b: "))
            c = float(input("Enter the coefficient c: "))
            result = solve_quadratic(a, b, c)
            if result is not None:
                print("Result: ", result)
        except ValueError:
            print("Error: invalid input")

    elif choice == "6":
        try:
            a = float(input("Enter the base:"))
            b = float(input("Enter the exponent:"))
            print("Result: ", calculate_exponentiation(a, b))
        except ValueError:
            print("Error: invalid input")

    elif choice == "7":
        try:
            a = float(input("Enter the base: "))
            b = float(input("Enter the number: "))
            answer = manual_logarithm(b, a)
            if answer is not None:
                print("Result: ", answer)
            else:
                print("Error: Invalid input")
        except ValueError:
            print("Error: invalid input")

    elif choice == "8":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")