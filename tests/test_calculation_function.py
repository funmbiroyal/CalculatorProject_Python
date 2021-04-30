import unittest
from CalculatorProject_Python.calculator_functions import product
from CalculatorProject_Python.calculator_functions import difference
from CalculatorProject_Python.calculator_functions import quotient

from CalculatorProject_Python.calculator_functions import add


class CalculatorFunctionTest(unittest.TestCase):
    def test_add_result(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(277777777, 50000000), 277777777 + 50000000)

    def test_add_result_type(self):
        self.assertIsInstance(add(2, 3), int)
        self.assertIsInstance(add(-2, -3), int)
        self.assertIsInstance(add(-2, 3), int)
        self.assertIsInstance(add(277777777, 50000000), int)

    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            add(2, "d")

    def test_multiply_result(self):
        self.assertEquals(product(3, 3), 9)
        self.assertEquals(product(5, 2), 10)
        self.assertEquals(product(100, 5), 500)

    def test_multiply_result_type(self):
        self.assertIsInstance(product(3, 3), int)
        self.assertIsInstance(product(5, 2), int)
        self.assertIsInstance(product(100, 5), int)

    def test_multiply_non_int_type(self):
        with self.assertRaises(TypeError):
            product(3, "j")

    def test_subtract_result(self):
        self.assertEqual(difference(56, 6), 50)
        self.assertEqual(difference(3, -9), 12)
        self.assertEqual(difference(34, 10), 24)

    def test_subtract_result_type(self):
        self.assertIsInstance(difference(56, 6), int)
        self.assertIsInstance(difference(3, -9), int)
        self.assertIsInstance(difference(34, 10), int)

    def test_subtract_non_int_type(self):
        with self.assertRaises(TypeError):
            difference(56, "u")

    def test_divide_result(self):
        self.assertEqual(quotient(30, 5), 6)
        self.assertEqual(quotient(15, 5), 3)
        self.assertEqual(quotient(20, 2), 10)

    def test_divide_result_type(self):
        self.assertIsInstance(quotient(30, 5), float)
        self.assertIsInstance(quotient(15, 5), float)
        self.assertIsInstance(quotient(34, 10), float)

    def test_divide_non_int_type(self):
        with self.assertRaises(TypeError):
            quotient(30, "r")

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            quotient(30, 0)


if __name__ == '__main__':
    unittest.main()
