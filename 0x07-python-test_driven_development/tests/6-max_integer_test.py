#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)

        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 0]), 1)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([5, 5, 5]), 5)

        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2, 4, 6]), 6)
        self.assertEqual(max_integer([1, 3, 5]), 5)

        self.assertEqual(max_integer([-100, 100]), 100)
        self.assertEqual(max_integer([2**31-1, -2**31]), 2**31-1)
if __name__ == '__main__':
    unittest.main()

