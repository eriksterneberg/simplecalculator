"""
Implements all pure and impure methods that make up the Simple Calculator showcase
"""

import re
from typing import Tuple
from numbers import Number
from collections import defaultdict

from .types_ import Command, Data
from .exceptions import InvalidInput
from .operations import operations


class SimpleCalculator:
    _memory_ = defaultdict(float)

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

    def parse(self, line: str) -> Tuple[Command, Data | Number]:
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

    def parse_store(self, register, op, val) -> Tuple[Command, Data]:
        if not re.match("\w*[a-z]\w*", register):
            raise InvalidInput("register was not alphanumeric with at least one letter")

        operation = operations.get(op)

        if operation is None:
            raise InvalidInput(f"'{op}' is not a supported operation")

        try:
            value = float(val)
        except ValueError:
            raise InvalidInput(f"'{val}' is not a valid value")

        return self.store, Data(target=register, operation=operation, value=value)

    def parse_print(self, command, register) -> Tuple[Command, Data | Number]:
        if command != "print":
            raise InvalidInput(f"bad syntax: '{command}' is not a valid command")

        return print, self.evaluate(register)

    def store(self, data: Data):
        pass

    def evaluate(self, register) -> Number:
        return self._memory_[register]
