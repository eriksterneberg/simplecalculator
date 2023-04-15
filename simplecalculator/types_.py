"""
Contains all custom datatypes used by Simple Calculator
"""

from typing import NewType, Callable
from collections import namedtuple


Data = namedtuple("Data", ["target", "operation", "value"])

Command = NewType('Command', Callable[[Data], None])
