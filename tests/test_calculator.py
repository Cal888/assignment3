"""
tests/test_calculator.py

Automated tests for the REPL calculator. 

Uses pytest's monkeypatch to simulate user input and StringIO to capture output.
Includes tests for addition, subtraction, multiplication, division, invalid inputs, 
invalid operators, and division by zero.
"""

import sys # Import python's standard library
from io import StringIO # Import to capture output as text
from app.calculator import calculator # Import the REPL calculator function

def run_calculator_with_input(monkeypatch, inputs):
    """Simulate user input and captures output from the REPL calculator."""
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Captures the output of the calculator
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator()
    sys.stdout = sys.__stdout__ # Reset stdout
    return captured_output.getvalue()

#------------------------------------------
# Simulate positive tests
#------------------------------------------

def test_calculator_addition(monkeypatch):
    """Test addition operation in REPL."""
    inputs = ["3 + 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 6.0" in output

def test_calculator_subtraction(monkeypatch):
    """Test subtraction operation in REPL."""
    inputs = ["5 - 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 2.0" in output

def test_calculator_multiplication(monkeypatch):
    """Test multiplication operation in REPL."""
    inputs = ["4 * 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 12.0" in output

def test_calculator_division(monkeypatch):
    """Test division operation in REPL."""
    inputs = ["30 / 10", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 3.0" in output

#------------------------------------------
# Simulate negative tests
#------------------------------------------

def test_invalid_operator(monkeypatch):
    """Test invalid operator in REPL."""
    inputs = ["8 % 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid operator. Please use one of these: +, -, *, or /" in output

def test_invalid_input_format(monkeypatch):
    """Test invalid input format in REPL."""
    inputs = ["five + one", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid input. Format: <number> <operator> <number>. Include spaces between each component." in output

def test_calculator_division_by_zero(monkeypatch):
    """Test division by zero in REPL."""
    inputs = ["3 / 0", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Division by zero is not allowed." in output