"""
Unit tests for the method evaluate
"""

import unittest

from simplecalculator.types_ import Thunk
from simplecalculator.operations import add, mul, sub
from simplecalculator import SimpleCalculator


class TestEvaluate_Simple(unittest.TestCase):

    def test_evaluate_missing_register(self):
        result = SimpleCalculator().evaluate("missing")
        self.assertEqual(result, 0)

    def test_evaluate_simple_operations_using_integers(self):
        calculator = SimpleCalculator()

        for thunk in Thunk("a", sub, 5), Thunk("a", mul, 2), Thunk("a", add, 50):
            calculator.store(thunk)

        # After having evaluated a value, it
        for _ in range(2):
            result = calculator.evaluate("a")
            self.assertEqual(result, 40)

    def test_evaluate_simple_operations_using_floats(self):
        calculator = SimpleCalculator()

        for thunk in Thunk("a", add, 1.3), Thunk("a", mul, 2):
            calculator.store(thunk)

        result = calculator.evaluate("a")
        self.assertEqual(result, 2.6)

class TestEvaluateRegistersAsValues(unittest.TestCase):

    def test_evaluate_register_as_value_happy_path(self):
        calculator = SimpleCalculator()

        thunks = [
            Thunk("result", add, "revenue"),
            Thunk("result", sub, "costs"),
            Thunk("revenue", add, 200),
            Thunk("costs", add, "salaries"),
            Thunk("salaries", add, 20),
            Thunk("salaries", mul,  5),
            Thunk("costs", add, 10),
        ]

        for thunk in thunks:
            calculator.store(thunk)

        self.assertEqual(calculator.evaluate("result"), 90)

    # def test_evaluate_register_as_value_circular(self):
    #     calculator = SimpleCalculator()
    #
    #     calculator.store(Thunk("a", add, "b"))
    #     calculator.store(Thunk("b", add, "a"))
    #     calculator.store(Thunk("a", add, 10))
    #     calculator.store(Thunk("b", add, 20))
    #
    #     self.assertEqual(calculator.evaluate("a"), 10)
    #     self.assertEqual(calculator.evaluate("b"), 20)
    #
