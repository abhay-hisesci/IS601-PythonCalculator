import unittest
import csv
from calculator import calculator

def csvFile(filename):
    fields = []
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    csvfile.close()
    return rows

class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calc = calculator()
        self.assertIsInstance(calc, calculator)

    def test_results_property(self):
        calc = calculator()
        self.assertEqual(calc.result, 1)

    def test_addition(self):
        calc = calculator()
        rows = csvFile("src/TestData/Unit Test Addition.csv")
        for row in rows:
            a = float(row[0])
            b = float(row[1])
            c = float(row[2])
            self.assertEqual(calc.add(a, b), c)

    def test_subtraction(self):
        calc = calculator()
        rows = csvFile("src/TestData/Unit Test Subtraction.csv")
        for row in rows:
            a = float(row[0])
            b = float(row[1])
            c = float(row[2])
            self.assertEqual(calc.subtract(a, b), c)

    def test_multiplication(self):
        calc = calculator()
        rows = csvFile("src/TestData/Unit Test Multiplication.csv")
        for row in rows:
            a = float(row[0])
            b = float(row[1])
            c = float(row[2])
            self.assertEqual(calc.multiply(a, b), c)

    def test_division(self):
        calc = calculator()
        rows = csvFile("src/TestData/Unit Test Division.csv")
        for row in rows:
            a = float(row[0])
            b = float(row[1])
            c = float(row[2])
            self.assertEqual(round(calc.divide(a, b), 9), c)

    def test_square(self):
        calc = calculator()
        rows = csvFile("src/TestData/Unit Test Square.csv")
        for row in rows:
            a = float(row[0])
            b = float(row[1])
            self.assertEqual(calc.square(a), b)

    def test_square_root(self):
        calc = calculator()
        rows = csvFile("src/TestData/Unit Test Square Root.csv")
        for row in rows:
            a = float(row[0])
            b = float(row[1])
            self.assertEqual(round(calc.square_root(a),8), round(b,8))

if __name__ == '__main__':
    unittest.main()