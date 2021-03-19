import unittest
from calculator import calculator

class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calc = calculator()
        self.assertIsInstance(calc, calculator)

    def test_results_property(self):
        calc = calculator()
        self.assertEqual(calc.result, 3)

if __name__ == '__main__':
    unittest.main()