"""
Implements all pure and impure methods that make up the Simple Calculator showcase
"""

import re
from typing import Tuple
from numbers import Number
from collections import defaultdict

from .types_ import Action, Actions, Thunk
from .exceptions import InvalidInput
from .operations import operations


class SimpleCalculator:
    """
    A showcase of how to implement a simple calculator with lazy evaluation
    """
    def __init__(self):
        self._thunks_ = defaultdict(list)
        self._values_ = defaultdict(int)

    def process(self, line: str) -> None:
        """
        Stores or prints values. Any value stored is evaluated only when printed.
        :param line: string input value from user
        :return: None
        """
        try:
            action, data = self.parse(line)
            action(data)
        except InvalidInput as e:
            print(e)  # log invalid input to console

    def parse(self, line: str) -> Tuple[Action, Thunk | Number]:
        """
        Returns a line parsed into an Action and a parameter to be fed into that action.

        A well-formed line of input has the following syntax:
        <register> <operation> <value> OR print <register>

        Examples of output:
            print 10                          # to be printed in the console
            self.store Thunk("a", add, 10)    # to be added into memory as a pending 'thunk'

        :param line: string input value from user
        :return: Action, Thunk | Number
        """
        if len(items := re.split("\\s+", line)) == 3:
            return self.parse_three_args(*items)
        elif len(items) == 2:
            return self.parse_two_args(*items)
        raise InvalidInput("bad syntax: only 2 or 3 arguments allowed, delimited by any amount of whitespace")

    def parse_three_args(self, register, op, val) -> Tuple[Action, Thunk]:
        """
        Currently only supports the <register> <operation> <value> command.
        Takes three arguments that signify the operation and its parameters that should be lazily executed.

        :param register: an alphanumeric value
        :param op: operation, such as add, mul or sub from the operator module in the standard library
        :param val: either a register or a number
        :return: Action and a Thunk
        """
        if not is_valid_register(register):
            raise InvalidInput("register was not alphanumeric with at least one letter")

        operation = operations.get(op)

        if operation is None:
            raise InvalidInput(f"'{op}' is not a supported operation")

        try:
            value = float(val)  # treat numbers as float to not lose decimals
        except ValueError:
            if not is_valid_register(val):
                raise InvalidInput(f"'{val}' is not a valid value")
            value = val

        return self.store, Thunk(target=register, op=operation, value=value)

    def parse_two_args(self, action, register) -> Tuple[Action, Number]:
        """
        Currently only supports the print <register> command.
        Evaluates registers as needed and prints to console

        :param action: currently only support the action 'print'
        :param register: register, will evaluate to zero if previously unseen
        :return: the built-in print function and a number
        """
        if action != Actions.PRINT:
            raise InvalidInput(f"bad syntax: '{action}' is not a valid action")

        return print, self.evaluate(register)

    def store(self, *thunks):
        """
        Store pending operations in memory
        :param thunks: variadic list of Thunk, to be added to pending operations
        :return: self, in order to be able to chain commands
        """
        for thunk in thunks:
            self._thunks_[thunk.target].append(thunk)
        return self

    def evaluate(self, register) -> Number:
        """
        Computes thunks pending for a register. Operates recursively and evaluates dependant values as needed.

        :param register: register
        :return: evaluated number, which is either an int or a float
        """
        value = self._values_[register]

        # Apply and clear the pending operations
        for t in self._thunks_.pop(register, []):
            try:
                # Apply recursive evaluation to evaluate dependencies
                value = t.op(value, t.value if isinstance(t.value, Number) else self.evaluate(t.value))
            except Exception as e:
                print(e)  # The input is rejected and the value is unchanged

        # Put evaluated value back into memory
        self._values_[register] = value

        # If a number is an int and not a float, remove the .0 from the output
        return integer if (integer := int(value)) == value else value


def is_valid_register(register: str) -> bool:
    """
    A valid register string is at least one character [a-z] preceded and followed by any number of alphanumeric strings

    :param register: an alphanumeric string
    :return: bool
    """
    return re.match("^[a-z0-9]*[a-z][a-z0-9]*$", register) is not None
