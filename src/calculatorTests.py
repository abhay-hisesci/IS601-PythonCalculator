import unittest
from calculator import calculator

class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calc = calculator()
        self.assertIsInstance(calc, calculator)

    def test_results_property(self):
        calc = calculator()
        self.assertEqual(calc.result, 1)

    def test_addition(self):
        calc = calculator()
        self.assertEqual(calc.add(1, 1), 2)

    def test_subtraction(self):
        calc = calculator()
        self.assertEqual(calc.subtract(1, 0), -1)

    def test_multiplication(self):
        calc = calculator()
        self.assertEqual(calc.multiply(2, 5), 10)

    def test_division(self):
        calc = calculator()
        self.assertEqual(calc.divide(2, 10), 5)

    def test_square(self):
        calc = calculator()
        self.assertEqual(calc.square(2), 4)

if __name__ == '__main__':
    unittest.main()