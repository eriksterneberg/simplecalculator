"""
All operations allowed by SimpleCalculator
"""

from operator import add, mul, sub  # Add 'truediv' here to support division in SimpleCalculator

# Allowed operations
# All operations must be of signature def operation(a, b) -> c
operations = {
    "add": add,
    "subtract": sub,
    "multiply": mul,
    # "divide": truediv,
}
