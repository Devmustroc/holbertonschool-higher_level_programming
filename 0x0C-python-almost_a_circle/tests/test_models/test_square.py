#!/usr/bin/python3
""" Module for test Square class """
import unittest
from unittest import TestCase
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import pycodestyle


class TestSquareMethods(unittest.TestCase):
    """ Suite to test Square class """

    def test_id(self):
        """ Test assigned id """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_new_squares(self):
        """ Test new squares """
        new = Square(1, 1)
        new2 = Square(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """ Test Square is a Base instance """
        new = Square(1)
        self.assertEqual(True, isinstance(new, Base))

    def test_is_Rectangle_instance(self):
        """ Test Square is a Rectangle instance """
        new = Square(1)
        self.assertEqual(True, isinstance(new, Rectangle))

    def test_no_arG_attrs_1(self):
        """ Test error raised with no args passed """
        with self.assertRaises(TypeError):
            new = Square()

    def test_acces_priv_attr_square(self):
        """test access to privates attributes"""
        new = Square(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_priv_square(self):
        """test access to privates attributes"""
        new = Square(1, 1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_priv_square2(self):
        """test access to privates attributes"""
        new = Square(1, 1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_priv_square3(self):
        """test access to privates attributes"""
        new = Square(1, 1)
        with self.assertRaises(AttributeError):
            new.__y


if __name__ == '__main__':
    unittest.main()
