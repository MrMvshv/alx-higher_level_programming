#!/usr/bin/python3
""" Unittest for Rectangle class
    methods
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    """ test initialization
        of rectangle
    """
    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_init(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(8, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_get_setters(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

        r.width = 10
        self.assertEqual(10, r.width)

        self.assertEqual(7, r.height)

        r.height = 10
        self.assertEqual(10, r.height)

        self.assertEqual(7, r.x)

        r.x = 10
        self.assertEqual(10, r.x)

        self.assertEqual(5, r.y)

        r.y = 10
        self.assertEqual(10, r.y)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)


if __name__ == '__main__':
    unittest.main()
