import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def set_up(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertEqual(self.calc.add(-3, -7), -10)
        self.assertEqual(self.calc.add(0, 0), 0)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(20, 3), 17)
        self.assertEqual(self.calc.subtract(-3, 5), -8)
        self.assertEqual(self.calc.subtract(-2, 0), -2)
        self.assertEqual(self.calc.subtract(-8, -8), 0)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(-6, 5), -30)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-4, -2), 8)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-4, 2), -2)
        self.assertEqual(self.calc.divide(10, -0.5), -20)
        self.assertEqual(self.calc.divide(0, -2), 0)
        self.assertEqual(self.calc.divide(10, 0))