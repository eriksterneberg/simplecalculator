"""
Unit tests for the method parse
"""

import unittest

from simplecalculator import SimpleCalculator, InvalidInput, Thunk, add


class TestParseZeroOrTooManyParams(unittest.TestCase):

    def test_parse_bad_number_of_arguments(self):
        for line in "", "a", "a b c d":
            with self.assertRaises(InvalidInput) as cm:
                SimpleCalculator().parse(line)

            self.assertEqual((str(cm.exception)), "bad syntax: only 2 or 3 arguments allowed, delimited by space")


class TestParseTwoParams(unittest.TestCase):

    def test_parse_bad_action(self):
        with self.assertRaises(InvalidInput) as cm:
            SimpleCalculator().parse("non_existant_action a")

        self.assertEqual("bad syntax: 'non_existant_action' is not a valid action", (str(cm.exception)))

    def test_happy_path(self):
        action, data = SimpleCalculator().parse("print a")

        self.assertEqual(print, action)
        self.assertEqual(0, data)

        action, data = SimpleCalculator().store(Thunk("a", add, 10)).parse("print a")

        self.assertEqual(print, action)
        self.assertEqual(10, data)


class TestParse3Params(unittest.TestCase):

    def test_register_not_alphanumeric(self):
        calculator = SimpleCalculator()

        for bad_register in "1", "_", "!":
            with self.assertRaises(InvalidInput) as cm:
                calculator.parse(f"{bad_register} operation value")

            self.assertEqual("register was not alphanumeric with at least one letter", str(cm.exception))

    def test_operation_not_supported(self):
        with self.assertRaises(InvalidInput) as cm:
            SimpleCalculator().parse("a unknown_operator value")

        self.assertEqual("'unknown_operator' is not a supported operation", str(cm.exception))

    def test_value_is_not_numeric(self):
        with self.assertRaises(InvalidInput) as cm:
            SimpleCalculator().parse("a add not_a_number_or_register")

        self.assertEqual("'not_a_number_or_register' is not a valid value", str(cm.exception))

    def test_happy_path_simple_integer(self):
        calculator = SimpleCalculator()

        action, data = calculator.parse("a add 10")

        self.assertEqual(calculator.store, action)
        self.assertEqual(Thunk("a", add, 10), data)

    def test_happy_path_register(self):
        calculator = SimpleCalculator()

        action, data = calculator.parse("a add b")

        self.assertEqual(calculator.store, action)
        self.assertEqual(Thunk("a", add, "b"), data)
