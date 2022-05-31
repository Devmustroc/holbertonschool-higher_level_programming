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
        if attrs is None:
            return self.__dict__
        ret_att = {}
        for key, val in self.__dict__.items():
            if key in attrs:
                ret_att[key] = value
        return ret_att

    def reload_form_json(self, json):
        """Replaces all attributes of the student instance"""
        for key, value in json.items():
            setattr(self, key, value)
