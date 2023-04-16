"""
Contains all custom datatypes used by Simple Calculator
"""

from typing import NewType, Callable
from collections import namedtuple


# Lazily evaluated operation(target, value)
Thunk = namedtuple("Thunk", ["target", "op", "value"])

# Action is either the print command which prints to console, or the store function,
# which simply stores the thunk in memory
Action = NewType('Action', Callable[[Thunk], None])


class Actions:
    """
    List of actions used by SimpleCalculator
    """
    QUIT = "quit"
    PRINT = "print"
