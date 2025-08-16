def calculator():
    """
    A simple calculator function that performs basic arithmetic operations.
    Supports addition, subtraction, multiplication, division, and power operations.
    """
    print("Welcome to the Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Exit")
    
    while True:
        try:
            # Get user input
            operation = input("\nEnter operation (1-6): ").strip()
            
            # Exit condition
            if operation == "6":
                print("Thank you for using the calculator!")
                break
            
            # Validate operation choice
            if operation not in ["1", "2", "3", "4", "5"]:
                print("Invalid operation! Please choose 1-6.")
                continue
            
            # Get numbers from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform calculation based on operation
            if operation == "1":
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif operation == "2":
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif operation == "3":
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif operation == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            elif operation == "5":
                result = num1 ** num2
                print(f"{num1} ** {num2} = {result}")
                
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

def calculate(operation, num1, num2):
    """
    A utility function that performs calculations without user interaction.
    
    Args:
        operation (str): The operation to perform ('+', '-', '*', '/', '**')
        num1 (float): First number
        num2 (float): Second number
    
    Returns:
        float: The result of the calculation
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ValueError("Cannot divide by zero!")
        return num1 / num2
    elif operation == '**':
        return num1 ** num2
    else:
        raise ValueError(f"Unsupported operation: {operation}")

# Example usage
if __name__ == "__main__":
    # Run the interactive calculator
    calculator()
    
    # Example of using the utility function
    print("\nExample calculations using the utility function:")
    print(f"5 + 3 = {calculate('+', 5, 3)}")
    print(f"10 - 4 = {calculate('-', 10, 4)}")
    print(f"6 * 7 = {calculate('*', 6, 7)}")
    print(f"15 / 3 = {calculate('/', 15, 3)}")
    print(f"2 ** 8 = {calculate('**', 2, 8)}")
