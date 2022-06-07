#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
from unittest import TestCase
from models.rectangle import Rectangle
from models.base import Base
import pycodestyle


class TestRectangleMethods(unittest.TestCase):
    """ Suite to test Rectangle class """

    def settingUp(self):
        """ Method  for each test """
        Base._Base__nb_objects = 0

    def test_new_rectangle_3(self):
        """test new rectangle"""
        rect = Rectangle(1, 1)
        rect2 = Rectangle(1, 1)
        self.assertEqual(False, rect is rect2)
        self.assertEqual(False, rect.id == rect2.id)

    def test_new_base_rectangle(self):
        """test rectangle is a base instance"""
        rect3 = Rectangle(1, 1)
        self.assertEqual(True, isinstance(rect3, Base))

    def test_numb_arg_rectangle(self):
        """test with only 1 arg passed"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1)

    def test_no_arg_rectangle(self):
        """test with no arg pased"""
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_acces_priv_attr_rectangle(self):
        """test Acces to a privates attributes"""
        rect = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rect.__width

    def test_acces_priv_attr_rectangle_2(self):
        """test Acces to a private attribute"""
        rect = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rect.__height

    def test_acces_priv_attr_rectangle_3(self):
        """test access to a privates attributes"""
        rect = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rect.__x

    def test_access_priv_attr_rectangle_4(self):
        """test acces to a privates attributes"""
        rect = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            rect.__y

    def test_stri_rectangle(self):
        """test for a string arg passed"""
        with self.assertRaises(TypeError):
            rect = Rectangle("4", 4, 4, 4, 4)

    def test_stri_rectangle_1(self):
        """test for a string arg passed"""
        with self.assertRaises(TypeError):
            rect = Rectangle(4, "4", 4, 4, 4)

    def test_stri_rectangle_2(self):
        """test for a string arg passed"""
        with self.assertRaises(TypeError):
            rect = Rectangle(4, 4, "4", 4, 4)

    def test_stri_rectangle_3(self):
        """test for a string arg passed"""
        with self.assertRaises(TypeError):
            rect = Rectangle(4, 4, 4, "4", 4)

    def test_value_attrs(self):
        """ test passing invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(0, 1)

    def test_value_attrs_1(self):
        """test passing invalid values"""
        with self.assertRaises(ValueError):
            new = Rectangle(1, 0)

    def test_value_attrs_3(self):
        """test passing invalid values"""
        with self.assertRaises(ValueError):
            new = Rectangle(-1, 0)

    def test_value_attrs_4(self):
        """test passing invalid values"""
        with self.assertRaises(ValueError):
            new = Rectangle(0, -1)


if __name__ == '__main__':
    unittest.main()
