"""
All operations allowed by SimpleCalculator
"""

from operator import add, mul, sub, truediv

# Allowed operations
# All operations must be of signature def operation(a, b) -> c
operations = {
    "add": add,
    "subtract": sub,
    "multiply": mul,
    "divide": truediv,
}
