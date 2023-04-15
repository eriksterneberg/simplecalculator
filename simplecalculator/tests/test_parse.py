"""
Unit tests for the method parse
"""

import unittest

from simplecalculator.exceptions import InvalidInput
from simplecalculator.types_ import Thunk
from simplecalculator.operations import add
from simplecalculator import SimpleCalculator


class TestParseZeroOrTooManyParams(unittest.TestCase):

    def test_parse_bad_number_of_arguments(self):
        for line in "", "a", "a b c d":

            with self.assertRaises(InvalidInput) as cm:
                SimpleCalculator().parse(line)

            self.assertEqual((str(cm.exception)), "bad syntax: only 2 or 3 arguments allowed, delimited by space")


class TestParseTwoParams(unittest.TestCase):

    def test_parse_bad_command(self):
        with self.assertRaises(InvalidInput) as cm:
            SimpleCalculator().parse("non_existant_command a")

        self.assertEqual((str(cm.exception)), "bad syntax: 'non_existant_command' is not a valid command")

    def test_happy_path(self):
        command, data = SimpleCalculator().parse("print a")

        self.assertEqual(command, print)
        self.assertEqual(data, 0)

        command, data = SimpleCalculator().store(Thunk("a", add, 10)).parse("print a")

        self.assertEqual(command, print)
        self.assertEqual(data, 10)


class TestParse3Params(unittest.TestCase):

    def test_register_not_alphanumeric(self):
        calculator = SimpleCalculator()

        for bad_register in "1", "_", "!":
            with self.assertRaises(InvalidInput) as cm:
                calculator.parse(f"{bad_register} operation value")

            self.assertEqual(str(cm.exception), "register was not alphanumeric with at least one letter")

    def test_operation_not_supported(self):
        with self.assertRaises(InvalidInput) as cm:
            SimpleCalculator().parse("a unknown_operator value")

        self.assertEqual(str(cm.exception), "'unknown_operator' is not a supported operation")

    def test_value_is_not_numeric(self):
        with self.assertRaises(InvalidInput) as cm:
            SimpleCalculator().parse("a add not_a_number")

        self.assertEqual(str(cm.exception), "'not_a_number' is not a valid value")

    def test_happy_path(self):
        calculator = SimpleCalculator()

        command, data = calculator.parse("a add 10")

        self.assertEqual(command, calculator.store)
        self.assertEqual(data, Thunk("a", add, 10))
