import unittest
from calculator import calculator

class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calc = calculator()
        self.assertIsInstance(calc, calculator)

    def test_addition(self):
        calc = calculator()
        self.assertEqual(calc.add(1, 1), 2)

    def test_subtraction(self):
        calc = calculator()
        self.assertEqual(calc.subtract(1, 1), 0)

    def test_results_property(self):
        calc = calculator()
        calc.add(2, 1)
        self.assertEqual(calc.result, 3)

if __name__ == '__main__':
    unittest.main()