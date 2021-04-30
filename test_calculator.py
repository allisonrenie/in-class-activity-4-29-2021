import unittest
import calculator

class test_class(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(3,4), 7)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(14,7), 7)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(7,11), 77)

    def test_divide(self):
        self.assertEqual(calculator.divide(21,3), 7)
        self.assertEqual(calculator.divide(7,0), 7)              #should fail

    # how to run:
    # python -m unittest test_calculator.py
