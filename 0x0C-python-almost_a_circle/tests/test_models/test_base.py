#!/usr/bin/python3
"""Defines  unittests for base.py
    methods
"""
import os
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""
    def setUp(self):
        """ nb_obj to 0, none arg
            id=4, none arg
        """
        Base._Base__nb_objects = 0
        self.b1 = Base()
        self.b2 = Base(None)
        self.b3 = Base(4)
        self.b4 = Base()
        self.b5 = Base()

    def tearDown(self):
        del self.b1
        del self.b2
        del self.b3
        del self.b4
        del self.b5

    def test_no_arg(self):
        self.assertEqual(self.b1.id, self.b2.id - 1)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_three_bases(self):
       self.assertEqual(self.b1.id, self.b4.id - 2)

    """ test id """
    def test_unique_id(self):
        self.assertEqual(self.b3.id, 4)

    def test_id_public(self):
        self.b4.id = 15
        self.assertEqual(15, self.b4.id)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)


if __name__ == "__main__":
    unittest.main()
