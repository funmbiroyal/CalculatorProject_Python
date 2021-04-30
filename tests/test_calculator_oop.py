import unittest
from CalculatorProject_Python.calculator_oop import Calculator


class CalculatorOopTest(unittest.TestCase):

    def test_add_result(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-2, -3), -5)
        self.assertEqual(Calculator.add(-2, 3), 1)
        self.assertEqual(Calculator.add(277777777, 50000000), 277777777 + 50000000)

    def test_add_result_type(self):
        self.assertIsInstance(Calculator.add(2, 3), int)
        self.assertIsInstance(Calculator.add(-2, -3), int)
        self.assertIsInstance(Calculator.add(-2, 3), int)
        self.assertIsInstance(Calculator.add(277777777, 50000000), int)

    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.add(2, "d")

    def test_multiply_result(self):
        self.assertEquals(Calculator.product(3, 3), 9)
        self.assertEquals(Calculator.product(5, 2), 10)
        self.assertEquals(Calculator.product(100, 5), 500)

    def test_multiply_result_type(self):
        self.assertIsInstance(Calculator.product(3, 3), int)
        self.assertIsInstance(Calculator.product(5, 2), int)
        self.assertIsInstance(Calculator.product(100, 5), int)

    def test_multiply_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.product(3, "j")

    def test_subtract_result(self):
        self.assertEqual(Calculator.difference(56, 6), 50)
        self.assertEqual(Calculator.difference(3, -9), 12)
        self.assertEqual(Calculator.difference(34, 10), 24)

    def test_subtract_result_type(self):
        self.assertIsInstance(Calculator.difference(56, 6), int)
        self.assertIsInstance(Calculator.difference(3, -9), int)
        self.assertIsInstance(Calculator.difference(34, 10), int)

    def test_subtract_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.difference(56, "u")

    def test_divide_result(self):
        self.assertEqual(Calculator.quotient(30, 5), 6)
        self.assertEqual(Calculator.quotient(15, 5), 3)
        self.assertEqual(Calculator.quotient(20, 2), 10)

    def test_divide_result_type(self):
        self.assertIsInstance(Calculator.quotient(30, 5), float)
        self.assertIsInstance(Calculator.quotient(15, 5), float)
        self.assertIsInstance(Calculator.quotient(34, 10), float)

    def test_divide_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.quotient(30, "r")

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            Calculator.quotient(30, 0)


if __name__ == '__main__':
    unittest.main()
