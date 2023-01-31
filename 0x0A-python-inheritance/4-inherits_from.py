#!/usr/bin/python3
"""
Method module
"""


def inherits_from(obj, a_class):
    """check if object is an instance of a class
    args:
        obj: object to check
        a_class: class to check
    return:
        True if object is an instance of a class
    """
    if type(obj) == a_class:  # if obj is an instance of a_class
        return False  # return False
    return all([issubclass(type(obj), a_class)])  # return True
