import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
        
    def test_addition(self):
        self.assertEqual(self.calc.add(5, 6), 11)
        self.assertEqual(self.calc.add(-5, 6), 1)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(11, 6), 5)
        self.assertEqual(self.calc.subtract(-5, 6), -11)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 6), 30)
        self.assertEqual(self.calc.multiply(-5, 6), -30)
    def test_division(self):
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(-16, 4), -4)
    
        