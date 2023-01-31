#!/usr/bin/python3
"""Module that defines the class Student"""


class Student:
    """class to create student instance"""

    def __init__(self, first_name, last_name, age): # constructor
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name # public instance attribute
        self.last_name = last_name # public instance attribute
        self.age = age # public instance attribute

    def to_json(self): # method to_json
        """Public method that retrieves a dictionary representation of a Student instance"""
        return self.__dict__.copy() # return dictionary representation of a Student instance
