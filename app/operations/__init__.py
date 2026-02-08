"""
app/operations.py

Defines the MathOperations class, which is responsible for providing basic mathematical operations:
addition, subtraction, multiplication, and division. 

Includes type hints for numeric inputs (integers or floats) and handles division
by zero by raising a ValueError.
"""

# Type alias allowing either integers or float values.
Number = int | float

class MathOperations:
    """Provide basic mathematical operations: addition, subtraction, multiplication, and division."""

    @staticmethod
    def addition(a: Number, b: Number) -> Number:
        """Return the sum of two numbers."""
        return a + b
    
    @staticmethod
    def subtraction(a: Number, b: Number) -> Number:
        """Return the difference of two numbers."""
        return a - b
    
    @staticmethod
    def multiplication(a: Number, b: Number) -> Number:
        """Return the product of two numbers."""
        return a * b
    
    @staticmethod
    def division(a: Number, b: Number) -> Number:
        """Return the quotient of two numbers."""
        try:
            return a / b
        except ZeroDivisionError as e: # Python raises this built-in exception when division by zero occurs.
            raise ValueError("Division by zero is not allowed.") from e # Re-raise as a ValueError to provide a custom user-friendly message.
