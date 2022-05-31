#!/usr/bin/python3
"""Module that defines the class Student"""


class Student:
    """class to create student instance"""

    def __init__(self, first_name, last_name, age):
        """Special method to intialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that returns directory description"""
        obj = self.__dict__.copy()
        for item in attrs:
            if type(item) != str:
                return obj

        d_list = {}

        for atr in range(len(attrs)):
            for satr in obj:
                if attrs[atr] == satr:
                    d_list[satr] = obj[satr]
            return obj
