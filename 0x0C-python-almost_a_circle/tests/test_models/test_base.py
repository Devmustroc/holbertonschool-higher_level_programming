#!/usr/bin/python3
"""Test Module for testing the base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """class for the tests"""

    def settingUp(self):
        """method for each test"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """test assigned id"""
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_base(self):
        """Testing nb object attribute"""
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        a = Base(3)
        self.assertEqual(a.id, 3)

    def test_multi_id(self):
        """test nb object attributes and assigned id"""
        new = Base()
        self.assertEqual(new.id, 3)
        new_1 = Base(1024)
        self.assertEqual(new_1.id, 1024)
        new_2 = Base()
        self.assertEqual(new_2.id, 4)

    def test_string_id(self):
        """ testing string id"""
        new_Str = Base('2')
        self.assertEqual(new_Str.id, '2')

    def test_more_args_id(self):
        """Test passing more args to init method"""
        with self.assertRaises(TypeError):
            new = Base(1, 1)
