# test_calculator.py
import unittest
from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertRaises(ValueError, divide, 10, 0)


if __name__ == '__main__':
    unittest.main()


# Understand the Test File
# Imports: The unittest module and functions from calculator.py are imported.
# Test Class: TestCalculator inherits from unittest.TestCase, which provides various assertion methods.
# Test Methods: Each method starting with test_ is a unit test. The self.assertEqual method checks if the first argument equals the second argument. The self.assertRaises method checks if the specified exception is raised.