"""
tests/test_operations.py

Parameterized tests for the MathOperations class: addition, subtraction,
multiplication, and division. Handles float precision errors and
checks that division by zero raises a ValueError.
"""

import pytest # Import the pytest framework for writing and running tests
from app.operations import MathOperations, Number # Import the MathOperations class and Number type alias

def assert_numeric_equal(result: Number, expected: Number) -> None:
    """Compare numeric results, rounding floats to 1 decimal place to fix precision errors."""
    if isinstance(result, float) or isinstance(expected, float):
        assert round(result, 1) == round(expected, 1)
    else:
        assert result == expected

#--------------------------------------
# Unit test for 'addition' method
#--------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 5, 10),             # Test adding two positive integers
        (-3, -4, -7),           # Test adding two negative integers
        (-8, 12, 4),            # Test adding a negative and positive integer
        (0, 0, 0),              # Test adding two zeros
        (1.2, 3.8, 5.0),        # Test adding two positive floats
        (-4.0, -2.5, -6.5),     # Test adding two negative floats
        (-3.2, 4.0, 0.8),       # Test adding a negative and positive float
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_negative_integers",
        "add_negative_and_positive_integer",
        "add_two_zeros",
        "add_two_positive_floats",
        "add_two_negative_floats",
        "add_negative_and_positive_float"
    ]
)

def test_addition(a: Number, b: Number, expected: Number) -> None:
    """Test addition of two numbers, including integers and floats."""
    result = MathOperations.addition(a, b)
    assert_numeric_equal(result, expected)

#--------------------------------------
# Unit test for 'subtraction' method
#--------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 2, 0),          # Test subtraction with two positive integers
        (-3, -1, -2),       # Test subtraction with two negative integers
        (-8, 3, -11),       # Test subtraction with a negative and positive integer
        (0, 0, 0),          # Test subtraction with two zeros
        (2.5, 1.5, 1.0),    # Test subtraction with two positive floats
        (-3.0, -2.0, -1.0), # Test subtraction with two negative floats
        (-5.0, 3.0, -8.0)   # Test subtraction with a negative and positive float
    ],
    ids=[
        "subtract_two_positive_integers",
        "subtract_two_negative_integers",
        "subtract_negative_and_positive_integer",
        "subtract_two_zeros",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
        "subtract_negative_and_positive_float"
    ]
)

def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    """Test subtraction of two numbers, including integers and floats."""
    result = MathOperations.subtraction(a, b)
    assert_numeric_equal(result, expected)

#--------------------------------------
# Unit test for 'multiplication' method
#--------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 3, 9),          # Test multiplication with two positive integers
        (-2, -2, 4),        # Test multiplication with two negative integers
        (-4, 3, -12),       # Test multiplication with a negative and positive integer
        (0, 0, 0),          # Test multiplication with two zeros
        (2.0, 3.0, 6.0),    # Test multiplication with two positive floats
        (-1.0, -3.0, 3.0),  # Test multiplication with two negative floats
        (-3.0, 8.0, -24.0)  # Test multiplication with a negative and positive float
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_two_negative_integers",
        "multiply_negative_and_positive_integer",
        "multiply_two_zeros",
        "multiply_two_positive_floats",
        "multiply_two_negative_floats",
        "multiply_negative_and_positive_float"
    ]
)

def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    """Test multiplication of two numbers, including integers and floats."""
    result = MathOperations.multiplication(a, b)
    assert_numeric_equal(result, expected)

#--------------------------------------
# Unit test for 'division' method
#--------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 2, 2),          # Test division with two positive integers
        (-4, -2, 2),        # Test division with two negative integers
        (-8, 2, -4),        # Test division with a negative and positive integer
        (3.0, 3.0, 1.0),    # Test division with two positive floats
        (-9.0, -3.0, 3.0),  # Test division with two negative floats
        (-12.0, 4.0, -3.0)  # Test division with a negative and positive float
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_two_negative_integers",
        "divide_negative_and_positive_integer",
        "divide_two_positive_floats",
        "divide_two_negative_floats",
        "divide_negative_and_positive_float"
    ]
)

def test_division(a: Number, b: Number, expected: Number) -> None:
    """Test division of two numbers, including integers and floats."""
    result = MathOperations.division(a, b)
    assert_numeric_equal(result, expected)

#--------------------------------------
# Negative Test Case : Division by Zero
#--------------------------------------

@pytest.mark.parametrize(
    "a, b",
    [
        (8, 0),            # Test division by zero with positive integer
        (-3, 0),           # Test division by zero with negative integer
        (5.0, 0),          # Test division by zero with positive float
        (-3.5, 0)          # Test division by zero with negative float
    ],
    ids=[
        "divide_by_zero_positive_integer",
        "divide_by_zero_negative_integer",
        "divide_by_zero_positive_float",
        "divide_by_zero_negative_float",
    ]
)

def test_division_by_zero(a: Number, b: Number) -> None:
    """Test that dividing by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        MathOperations.division(a, b)





