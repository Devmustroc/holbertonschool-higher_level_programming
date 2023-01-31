#!/usr/bin/python3
"""
A model that contains a Base class to manage
the id attribute of all classes that extend
from Base and avoid duplicate the same code.
"""

from os import path
import json
import csv


class Base:
    """It's a base class for all other classes"""
    __nb_objects = 0 # private class attribute

    def __init__(self, id=None): # public instance attribute
        """Constructor method"""

        if id is None: # if id is not given
            Base.__nb_objects += 1 # increment the private class attribute
            self.id = Base.__nb_objects # assign the private class attribute
        else: # if id is given
            self.id = id # assign the public instance attribute

    @staticmethod # decorator
    def to_json_string(list_dictionaries): # static method
        if list_dictionaries is None or len(list_dictionaries) == 0: # if list_dictionaries is None or empty
            return '[]' # return an empty list

        return json.dumps(list_dictionaries)

    @classmethod # decorator
    def save_to_file(cls, list_objs): # class method
        filename = cls.__name__ + '.json' # create a filename

        with open(filename, mode='w', encoding='utf-8') as f:   # open the file
            if list_objs is None: # if list_objs is None
                return f.write(cls.to_json_string(None)) # return an empty list

            json_attrs = [] # create an empty list

            for elem in list_objs: # iterate over list_objs
                json_attrs.append(elem.to_dictionary()) # append the dictionary representation of each element

            return f.write(cls.to_json_string(json_attrs)) # return the list of dictionaries

    @staticmethod # decorator
    def from_json_string(json_string): # static method
        if json_string is None or len(json_string) == 0: # if json_string is None or empty
            return [] # return an empty list

        return json.loads(json_string)  # return the list of the JSON string representation

    @classmethod # decorator
    def create(cls, **dictionary): # class method
        if cls.__name__ == 'Square': # if the class name is Square
            dummy = cls(3) # create a dummy instance

        if cls.__name__ == 'Rectangle':   # if the class name is Rectangle
            dummy = cls(3, 3)   # create a dummy instance

        dummy.update(**dictionary) # update the dummy instance with the dictionary
        return dummy # return the dummy instance

    @classmethod # decorator
    def load_from_file(cls): # class method
        """
        This function returns a list
        of instances
        """
        filename = cls.__name__ + '.json' # create a filename

        if path.exists(filename) is False: # if the file doesn't exist
            return [] # return an empty list

        with open(filename, mode='r', encoding='utf-8') as f: # open the file
            objs = cls.from_json_string(f.read()) # read the file and convert it to a list of dictionaries
            instances = [] # create an empty list

            for elem in objs:   # iterate over the list of dictionaries
                instances.append(cls.create(**elem)) # create an instance with each dictionary and append it to the list

            return instances # return the list of instances

    @classmethod # decorator
    def save_to_file_csv(cls, list_objs):   # class method
        """It's a class method that serializes in CSV"""
        fn = cls.__name__ + ".csv" # create a filename
        if fn == "Rectangle.csv": # if the filename is Rectangle.csv
            fields = ["id", "width", "height", "x", "y"]   # create a list of fields
        else:   # if the filename is Square.csv
            fields = ["id", "size", "x", "y"]   # create a list of fields
        with open(fn, mode="w", newline="") as myFile:  # open the file
            if list_objs is None:   # if list_objs is None
                writer = csv.writer(myFile) # create a writer
                writer.writerow([[]])   # write an empty list
            else:   # if list_objs is not None
                writer = csv.DictWriter(myFile, fieldnames=fields)  # create a writer
                writer.writeheader()    # write the header
                for x in list_objs: # iterate over list_objs
                    writer.writerow(x.to_dictionary())  # write each dictionary representation of each element
