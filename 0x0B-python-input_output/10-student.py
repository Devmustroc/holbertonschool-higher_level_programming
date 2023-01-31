#!/usr/bin/python3
"""Module that defines the class Student"""


class Student: # class Student
    """class to create student instance"""

    def __init__(self, first_name, last_name, age): # constructor
        """Instantiation with first_name, last_name and age"""
        self.age = age  # public instance attribute
        self.last_name = last_name # public instance attribute
        self.first_name = first_name # public instance attribute

    def to_json(self, attrs=None): # method to_json
        """Public method that retrieves a dictionary representation of a Student instance"""
        if attrs is None: # if attrs is None
            return self.__dict__ # return dictionary representation of a Student instance
        re_att = {} # empty dictionary
        for key, val in self.__dict__.items(): # loop through dictionary
            if key in attrs: # if key in attrs
                re_att[key] = val # add key and value to dictionary
        return re_att # return dictionary
