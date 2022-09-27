
def add(a, b):
    """
    Add two numbers
    """
    return a + b


def subtract(a, b):
    """
    Subtract two numbers
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers
    """
    return a * b


def divide(a, b):
    """
    Divide two numbers
    """
    return a / b


def main():
    """
    Main function for calculator.py.  Runs the calculator program.
    """

    # Print welcome message to user.  Get first number from user.
    print("Welcome to the calculator program.")

    num1 = float(input("Please enter the first number: "))

    # Get operator from user.  Get second number from user.  Perform operation.  Print result.  Repeat until user exits.
    while True:

        operator = input("Please enter an operator (+, -, *, /, or q to quit): ")

        if operator == "q":
            break

        num2 = float(input("Please enter the second number: "))

        if operator == "+":
            print(add(num1, num2))

        elif operator == "-":
            print(subtract(num1, num2))

        elif operator == "*":
            print(multiply(num1, num2))

        elif operator == "/":
            print(divide(num1, num2))

        else:
            print("Invalid operator.")

        num1 = float(input("Please enter the first number: "))

    # Print goodbye message to user.  Exit program.
    print("Thank you for using the calculator program.")


if __name__ == "__main__":

    main()
