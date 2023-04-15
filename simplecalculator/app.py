"""
Implements all pure and impure methods that make up the Simple Calculator showcase
"""

import re
from typing import Tuple
from numbers import Number
from collections import defaultdict

from .types_ import Command, Thunk
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
            command, data = self.parse(line)
            command(data)
        except InvalidInput as e:
            print(e)

    def parse(self, line: str) -> Tuple[Command, Thunk | Number]:
        """
        A pure function which only returns parsed input but does nothing,  with it, in order to make it easier to test using UT

        A well-formed line of input has the following syntax:
        <register> <operation> <value>

        :param line: string input value from user
        :return: (Command, Data), where the Command
        """
        items = line.split(" ")

        if len(items) == 3:
            return self.parse_store(*items)

        if len(items) == 2:
            return self.parse_print(*items)

        raise InvalidInput("bad syntax: only 2 or 3 arguments allowed, delimited by space")

    def parse_store(self, register, op, val) -> Tuple[Command, Thunk]:
        if not is_valid_register(register):
            raise InvalidInput("register was not alphanumeric with at least one letter")

        operation = operations.get(op)

        if operation is None:
            raise InvalidInput(f"'{op}' is not a supported operation")

        try:
            value = float(val)
        except ValueError:
            if is_valid_register(val):
                value = val
            else:
                raise InvalidInput(f"'{val}' is not a valid value")

        return self.store, Thunk(target=register, operation=operation, value=value)

    def parse_print(self, command, register) -> Tuple[Command, Thunk | Number]:
        if command != "print":
            raise InvalidInput(f"bad syntax: '{command}' is not a valid command")

        return print, self.evaluate(register)

    def store(self, *thunks):
        """
        Store pending operations in memory
        :param thunks: variadic list of Thunk, to be added to pending operations
        :return:
        """
        for thunk in thunks:
            self._thunks_[thunk.target].append(thunk)
        return self

    def evaluate(self, register) -> Number:

        # apply and clear the pending operations
        for thunk in self._thunks_.pop(register, []):
            try:
                # Apply recursive evaluation to evaluate dependencies
                right = thunk.value if isinstance(thunk.value, Number) else self.evaluate(thunk.value)
                self._values_[register] = thunk.operation(self._values_[register], right)
            except Exception as e:
                print(e)  # The input is rejected and the value is unchanged

        # If a number is an int and not a float, remove the .0 from the output
        value = self._values_[register]
        return integer if (integer := int(value)) == value else value


def is_valid_register(register: str) -> bool:
    """
    A valid register string is at least one character [a-z] preceeded and followed by any numnber of
    alphanumeric strings [a-z0-9]

    :param register:
    :return: bool
    """
    return re.match('^[a-z0-9]*[a-z][a-z0-9]*$', register) is not None
