"""
robust_division_calculator.py

Contains a single function safe_divide that attempts to:
- Convert inputs to floats
- Perform division
- Handle ZeroDivisionError and ValueError
"""

def safe_divide(numerator, denominator):
    """
    Divide numerator by denominator with robust error handling.

    Parameters:
    - numerator:   str or number (will be coerced to float)
    - denominator: str or number (will be coerced to float)

    Returns:
    - On success:  "The result of the division is X"
    - On zero   :  "Error: Cannot divide by zero."
    - On non-numeric input: "Error: Please enter numeric values only."
    """
    # 1. Convert to floats
    try:
        num = float(numerator)
        den = float(denominator)
    except (TypeError, ValueError):
        return "Error: Please enter numeric values only."

    # 2. Perform division and handle division by zero
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # 3. Format and return the result
    return f"The result of the division is {result}"
