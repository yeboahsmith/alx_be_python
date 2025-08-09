
# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---- Addition Tests ----
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_sign_numbers(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_addition_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 3.2), 5.7)

    # ---- Subtraction Tests ----
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtraction_mixed_sign_numbers(self):
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_subtraction_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # ---- Multiplication Tests ----
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, -3), 12)

    def test_multiplication_mixed_sign_numbers(self):
        self.assertEqual(self.calc.multiply(-4, 3), -12)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_multiplication_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)

    # ---- Division Tests ----
    def test_division_positive_numbers(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-6, -3), 2)

    def test_division_mixed_sign_numbers(self):
        self.assertEqual(self.calc.divide(-6, 3), -2)

    def test_division_with_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_floats(self):
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))

if __name__ == "__main__":
    unittest.main()
