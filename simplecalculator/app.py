"""
Implements all pure and impure methods that make up the Simple Calculator showcase
"""

import re
from typing import Tuple
from numbers import Number
from collections import defaultdict

from .types_ import Action, Thunk
from .exceptions import InvalidInput
from .operations import operations


class SimpleCalculator:

    def __init__(self):
        self._thunks_ = defaultdict(list)
        self._values_ = defaultdict(int)

    def process(self, line: str) -> None:
        """
        Stores or prints (evaluates stored) lazy values

        :param line: string input value from user
        :return: None
        """
        try:
            action, data = self.parse(line)
            action(data)
        except InvalidInput as e:
            print(e)

    def parse(self, line: str) -> Tuple[Action, Thunk | Number]:
        """
        A pure function which returns an Action and a Thunk or Number. This is a pure function, to make UT easier.

        A well-formed line of input has the following syntax:
        <register> <operation> <value>

        :param line: string input value from user
        :return: (Action, Data), where the Action
        """
        items = line.split(" ")

        if len(items) == 3:
            return self.parse_store(*items)

        if len(items) == 2:
            return self.parse_print(*items)

        raise InvalidInput("bad syntax: only 2 or 3 arguments allowed, delimited by space")

    def parse_store(self, register, op, val) -> Tuple[Action, Thunk]:
        if not is_valid_register(register):
            raise InvalidInput("register was not alphanumeric with at least one letter")

        operation = operations.get(op)

        if operation is None:
            raise InvalidInput(f"'{op}' is not a supported operation")

        try:
            value = float(val)  # treat numbers as float to not lose decimals
        except ValueError:
            if is_valid_register(val):
                value = val
            else:
                raise InvalidInput(f"'{val}' is not a valid value")

        return self.store, Thunk(target=register, operation=operation, value=value)

    def parse_print(self, action, register) -> Tuple[Action, Thunk | Number]:
        if action != "print":
            raise InvalidInput(f"bad syntax: '{action}' is not a valid action")

        return print, self.evaluate(register)

    def store(self, *thunks):
        """
        Store pending operations in memory
        :param thunks: variadic list of Thunk, to be added to pending operations
        :return: self
        """
        for thunk in thunks:
            self._thunks_[thunk.target].append(thunk)
        return self

    def evaluate(self, key) -> Number:
        """
        Computes thunks pending for a register. Operates recursively and evaluates dependant values as needed.

        :param key: either register or value
        :return: evaluated number, which is an int or a float
        """
        if isinstance(key, Number):
            return key

        register = key
        value = self._values_[register]

        # Apply and clear the pending operations
        for thunk in self._thunks_.pop(register, []):
            try:
                # Apply recursive evaluation to evaluate dependencies
                value = thunk.operation(value, self.evaluate(thunk.value))
            except Exception as e:
                print(e)  # The input is rejected and the value is unchanged

        # Put evaluated value back into memory
        self._values_[register] = value

        # If a number is an int and not a float, remove the .0 from the output
        return integer if (integer := int(value)) == value else value


def is_valid_register(register: str) -> bool:
    """
    A valid register string is at least one character [a-z] preceded and followed by any number of alphanumeric strings

    :param register:
    :return: bool
    """
    return re.match('^[a-z0-9]*[a-z][a-z0-9]*$', register) is not None
