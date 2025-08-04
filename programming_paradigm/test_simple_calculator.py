import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(SimpleCalculator.add(10, 5), 15)
        self.assertEqual(SimpleCalculator.add(-2, 3), 1)
        self.assertEqual(SimpleCalculator.add(-3, -7), -10)
        self.assertEqual(SimpleCalculator.add(0, 0), 0)
    def test_subtraction(self):
        self.assertEqual(SimpleCalculator.subtract(20, 3), 17)
        self.assertEqual(SimpleCalculator.subtract(-3, 5), -8)
        self.assertEqual(SimpleCalculator.subtract(-2, 0), -2)
        self.assertEqual(SimpleCalculator.subtract(-8, -8), 0)
    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(10, 5), 50)
        self.assertEqual(SimpleCalculator.multiply(-6, 5), -30)
        self.assertEqual(SimpleCalculator.multiply(0, 5), 0)
        self.assertEqual(SimpleCalculator.multiply(-4, -2), 8)
    def test_divide(self):
        self.assertEqual(SimpleCalculator.divide(10, 2), 5)
        self.assertEqual(SimpleCalculator.divide(-4, 2), -2)
        self.assertEqual(SimpleCalculator.divide(10, -0.5), -20)
        self.assertEqual(SimpleCalculator.divide(0, -2), 0)
        self.assertEqual(SimpleCalculator.divide(10, 0))