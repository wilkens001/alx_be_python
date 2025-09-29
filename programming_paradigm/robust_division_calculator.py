#!/usr/bin/python3
"""
This module contains a robust division calculator that handles various error cases.
"""


def safe_divide(numerator, denominator):
    """
    Safely performs division between two numbers with comprehensive error handling.

    Args:
        numerator: The number to be divided (dividend)
        denominator: The number to divide by (divisor)

    Returns:
        str: A message indicating the result or describing an error that occurred
    """
    try:
        # Convert string inputs to float
        num = float(numerator)
        den = float(denominator)

        # Check for division by zero
        if den == 0:
            return "Error: Cannot divide by zero."

        # Perform division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."
    except Exception as e:
        # Handle any unexpected errors
        return f"Error: An unexpected error occurred: {str(e)}"