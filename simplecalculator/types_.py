"""
Contains all custom datatypes used by Simple Calculator
"""

from typing import NewType, Callable
from collections import namedtuple


# Lazily evaluated target, operation and value
Thunk = namedtuple("Thunk", ["target", "operation", "value"])

Command = NewType('Command', Callable[[Thunk], None])
