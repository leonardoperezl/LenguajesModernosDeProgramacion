from calculator import Calculator

def main():
    calc = Calculator()

    while True:
        print("\nSimple Calculator")
        print("Available operations: add, sub, mul, div")
        operation = input("Enter operation (or 'exit' to quit): ").strip().lower()

        if operation == "exit":
            print("Goodbye!")
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = calc.calculate(operation, a, b)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
