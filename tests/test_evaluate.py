"""
Unit tests for the method evaluate
"""

import unittest

from simplecalculator import Thunk, add, mul, sub, SimpleCalculator


class TestEvaluateSimple(unittest.TestCase):

    def test_evaluate_missing_register(self):
        result = SimpleCalculator().evaluate("missing")
        self.assertEqual(0, result)

    def test_evaluate_simple_operations_using_integers(self):
        calculator = SimpleCalculator().store(
            Thunk("a", sub, 5),
            Thunk("a", mul, 2),
            Thunk("a", add, 50),
        )

        # After having evaluated a value, it
        for _ in range(2):
            self.assertEqual(40, calculator.evaluate("a"))

    def test_evaluate_simple_operations_using_floats(self):
        result = SimpleCalculator().store(Thunk("a", add, 1.3), Thunk("a", mul, 2)).evaluate("a")
        self.assertEqual(2.6, result)


class TestEvaluateRegistersAsValues(unittest.TestCase):

    def test_evaluate_register_as_value_happy_path_1(self):
        calculator = SimpleCalculator().store(
            Thunk("a", add, 10),
            Thunk("b", add, "a"),
            Thunk("b", add, 1),
        )

        self.assertEqual(11, calculator.evaluate("b"))

    def test_evaluate_register_as_value_happy_path_2(self):
        calculator = SimpleCalculator().store(
            Thunk("result", add, "revenue"),
            Thunk("result", sub, "costs"),
            Thunk("revenue", add, 200),
            Thunk("costs", add, "salaries"),
            Thunk("salaries", add, 20),
            Thunk("salaries", mul, 5),
            Thunk("costs", add, 10),
        )

        self.assertEqual(90, calculator.evaluate("result"))

    def test_evaluate_register_as_value_circular(self):
        calculator = SimpleCalculator().store(
            Thunk("a", add, "b"),
            Thunk("b", add, "a"),
            Thunk("a", add, 10),
            Thunk("b", add, 20),
        )

        # When 'a' is evaluated, 'b' is first evaluated to 0 + 20 = 20. Later 10 is added, which makes a = 30
        self.assertEqual(calculator.evaluate("a"), 30)

        # When 'b' is evaluated below, all pending thunks have already been calculated. When 'b' was evaluated, 'a'
        # was zero because all thunks for 'a' had been evaluated, so b = 20.
        self.assertEqual(calculator.evaluate("b"), 20)
