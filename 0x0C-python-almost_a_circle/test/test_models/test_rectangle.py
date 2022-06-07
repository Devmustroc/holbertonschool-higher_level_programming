#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
from unittest import TestCase
from models.rectangle import Rectangle
from models.base import Base
import pycodestyle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_is_class(self):
        """ obj id increments """
        r1 = Rectangle(2, 2, 3, 1)
        self.assertTrue(type(r1) is Rectangle and issubclass(Rectangle, Base))

        r2 = Rectangle(2, 6, 4, 2)
        self.assertIsInstance(r2, Rectangle)

    def test_2_values(self):
        """checks for valid input """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_3_values(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 7)
        r3 = Rectangle(10, 2, 16)
        self.assertEqual(r1.id, r3.id - 2)

    def test_4_values(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 7)
        r3 = Rectangle(10, 2, 16)
        r4 = Rectangle(10, 2, 16, 5)
        self.assertEqual(r1.id, r4.id - 3)

    def test_5_values(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 7)
        r3 = Rectangle(10, 2, 16)
        r4 = Rectangle(10, 2, 16, 5)
        r5 = Rectangle(10, 2, 16, 5, 53)
        self.assertEqual(53, Rectangle(10, 2, 16, 5, 53).id)

    def str_arg(self):
        r7 = Rectangle(1, 11, 1, 1, "Python")
        self.assertEqual(r7.id, "python")

    def test_value_error(self):
        """
        Test for checking value error
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2)
            Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -2)
            Rectangle(1, 0)

    def one_arg(self):
        """checks for valid error"""
        with self.assertRaises(TypeError):
            Rectangle()

    def none_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(7, None)
            Rectangle(None, 6)

    def str_two_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "4")

    def str_zero_arg(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def str_zero_arg(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def str_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 16, "Holberton")
            Rectangle(10, 2, 16, "Betty", "Holberton")

    def zero_arg(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 0, 0, 0, 0)

    def float_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2.0, 1, 1, 12)

    def six_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, 1, 12, 5)


if __name__ == '__main__':
    unittest.main()
