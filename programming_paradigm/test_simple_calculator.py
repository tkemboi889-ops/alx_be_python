# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        

    def test_subtraction(self):
        
        self.assertEqual(self.calc.subtract(10, 5), 5)
        

    def test_multiplication(self):
        
        self.assertEqual(self.calc.multiply(2, 3), 6)
        

    def test_division(self):
       
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)

        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

if __name__ == "__main__":
    unittest.main()
