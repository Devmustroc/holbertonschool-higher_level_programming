#!/usr/bin/python3
"""Class to JSON module"""


def class_to_json(obj): # function class_to_json
    """
    Returns the dictionary description with simple
    data structure (list, dict, string, integer
    and boolean) for JSON serialization of an object.
    """
    return obj.__dict__ # return dictionary description with simple data structure
