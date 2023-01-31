#!/usr/bin/python3
"""Module that defines the class Student"""


class Student:
    """class to create student instance"""

    def __init__(self, first_name, last_name, age): # constructor
        """Instantiation with first_name, last_name and age"""
        self.last_name = last_name # public instance attribute
        self.first_name = first_name # public instance attribute
        self.age = age # public instance attribute

    def to_json(self, attrs=None): # method to_json
        """Public method that retrieves a dictionary representation of a Student instance"""
        if attrs is None: # if attrs is None
            return self.__dict__ # return dictionary representation of a Student instance
        ret_att = {} # empty dictionary
        for key, value in self.__dict__.items(): # loop through dictionary
            if key in attrs: # if key in attrs
                ret_att[key] = value # add key and value to dictionary
        return ret_att # return dictionary

    def reload_from_json(self, json): # method reload_from_json
        """Public method that replaces all attributes of the Student instance"""
        for atr in json: # loop through json
            self.__dict__[atr] = json[atr] # add key and value to dictionary
