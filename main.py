#!/usr/bin/env python3
"""
Main script to demonstrate the calculator functionality.
This file imports and uses the calculator functions from calculator.py
"""

from calculator import calculator, calculate

def main():
    """
    Main function that demonstrates different ways to use the calculator.
    """
    print("=" * 50)
    print("CALCULATOR DEMONSTRATION")
    print("=" * 50)
    
    # Option 1: Run the interactive calculator
    print("\n1. Running Interactive Calculator:")
    print("-" * 30)
    calculator()
    
    # Option 2: Use the utility function for specific calculations
    print("\n2. Using Utility Function for Specific Calculations:")
    print("-" * 50)
    
    # Example calculations
    calculations = [
        ("Addition", "+", 15, 25),
        ("Subtraction", "-", 100, 30),
        ("Multiplication", "*", 12, 8),
        ("Division", "/", 50, 5),
        ("Power", "**", 2, 10)
    ]
    
    for operation_name, op, num1, num2 in calculations:
        try:
            result = calculate(op, num1, num2)
            print(f"{operation_name}: {num1} {op} {num2} = {result}")
        except ValueError as e:
            print(f"Error in {operation_name}: {e}")
    
    # Option 3: Get user input for custom calculations
    print("\n3. Custom Calculations:")
    print("-" * 25)
    
    while True:
        try:
            # Get operation from user
            print("\nAvailable operations: +, -, *, /, **")
            operation = input("Enter operation (or 'quit' to exit): ").strip().lower()
            
            if operation == 'quit':
                break
            
            if operation not in ['+', '-', '*', '/', '**']:
                print("Invalid operation! Please use +, -, *, /, or **")
                continue
            
            # Get numbers from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform calculation
            result = calculate(operation, num1, num2)
            print(f"Result: {num1} {operation} {num2} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
    
    print("\nThank you for using the calculator!")

if __name__ == "__main__":
    main()
