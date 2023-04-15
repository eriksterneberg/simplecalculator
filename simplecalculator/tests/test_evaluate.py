"""
Unit tests for the method evaluate
"""

import unittest

from simplecalculator.types_ import Thunk
from simplecalculator.operations import add, mul, sub
from simplecalculator import SimpleCalculator


class TestEvaluate(unittest.TestCase):

    def test_evaluate_missing_register(self):
        result = SimpleCalculator().evaluate("missing")
        self.assertEqual(result, 0)

    def test_evaluate_simple_operations(self):
        calculator = SimpleCalculator()

        for thunk in Thunk("a", sub, 5), Thunk("a", mul, 2), Thunk("a", add, 50):
            calculator.store(thunk)

        # After having evaluated a value, it
        for _ in range(2):
            result = calculator.evaluate("a")
            self.assertEqual(result, 40)
