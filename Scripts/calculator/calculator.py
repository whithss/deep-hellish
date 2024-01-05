class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        else:
            return a / b


def main():
    calculator = Calculator()

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = input("Enter number (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '1':
        print("Result:", calculator.add(num1, num2))
    elif operation == '2':
        print("Result:", calculator.subtract(num1, num2))
    elif operation == '3':
        print("Result:", calculator.multiply(num1, num2))
    elif operation == '4':
        print("Result:", calculator.divide(num1, num2))
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()