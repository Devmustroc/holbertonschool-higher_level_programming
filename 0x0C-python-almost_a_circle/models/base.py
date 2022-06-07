#!/usr/bin/python3
"""Base Class Module"""

import os.path
from fileinput import filename
import json
import csv


class Base:
    """Class parent of all class in the project"""
    __nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        f_name = cls.__name__+'.json'
        dic = []
        if list_objs is not None:
            dic = [a.to_dictionary() for a in list_objs]
        with open(f_name, 'w') as f:
            f.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None and not json_string:
            return []
        return json.loads(json_string)
