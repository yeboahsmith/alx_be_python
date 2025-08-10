import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------- ADDITION ----------
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.3), 3.8)

    # ---------- SUBTRACTION ----------
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(3.2, 1.1), 2.1)

    # ---------- MULTIPLICATION ----------
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 3), -9)
        self.assertEqual(self.calc.multiply(0, 9999), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(-2.5, -4), 10.0)

    # ---------- DIVISION ----------
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == '__main__':
    unittest.main()
