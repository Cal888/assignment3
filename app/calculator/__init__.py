"""
app/calculator.py

A REPL calculator that performs addition, subtraction,
multiplication, and division using the MathOperations class.
"""
from app.operations import MathOperations # Import the MathOperations class

def calculator():
    
    """
    REPL calculator that takes user input and performs basic mathematical
    operations: addition, subtraction, multiplication, and division.
    """
    # Using a dictionary instead of if, elif, else statements to reduce repetitiveness and lengthy code. 
    # Mapping operators to MathOperations methods.
    # Defined outside the loop so the dictionary is created only once.
    operators = {
        '+': MathOperations.addition,
        '-': MathOperations.subtraction,
        '*': MathOperations.multiplication,
        '/': MathOperations.division
    }

    # Welcome user to the calculator and provide an option to exit.
    print("Welcome to the REPL calculator! Type 'exit' to quit")

    while True: # Run REPL calculator until prompted to exit by user

        # Collecting user input to use for calculation and removing extra space before and after actual calculation components.
        user_input = input("Please enter a calculation: ").strip()

        # If the user types 'exit' in any casing, it will be converted to lowercase, and then print the message and stop the calculator.
        if user_input.lower() == 'exit':
            print("Exiting the calculator...")
            break # Exits the calculator
        
        try:
            # Split the string input into 3 variables on space
            num1_str, operator, num2_str = user_input.split()
            # Convert string inputs to floats
            num1, num2 = float(num1_str), float(num2_str)
        except ValueError:
            # This error will be thrown if the user types less, or more than 3 arguments.
            # An error will be thrown if the user does not include spaces between each argument.
            # Another error will be thrown if there is a string that is unable to convert to float.
            print("Invalid input. Format: <number> <operator> <number>. Include spaces between each component.")
            continue # Prompts user to try again: this bring the user back to the top of the loop

        if operator not in operators:
            # If operator is not found in the 'operators' dictionary, the message will show, and return the user to the top of loop.
            print("Invalid operator. Please use one of these: +, -, *, or /")
            continue # Prompts user to try again: this bring the user back to the top of the loop

        try:
            # Stores the mathematical operation if valid.
            result = operators[operator](num1, num2) # An example would be operators['+'] == MathOperations.addition(num1, num2).
        except ValueError as e:
            # This error is specifically for division by zero. The message will be shown to the user and prompted to try again.
            print(e) # Display the custom division by zero error message.
            continue # Prompts user to try again: this bring the user back to the top of the loop
            
        # Prints the final result. An example would be 2 + 2 == 4.0
        print(f"Result: {result}")

