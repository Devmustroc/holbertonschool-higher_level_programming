#!/usr/bin/python3
"""Module that defines the class Student"""


class Student:
    """class to create student instance"""

    def __init__(self, first_name, last_name, age):
        """Special method to intialize"""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """Method that returns directory description"""
        if attrs is None:
            return self.__dict__
        re_att = {}
        for key, val in self.__dict__.items():
            if key in attrs:
                re_att[key] = val
        return re_att
