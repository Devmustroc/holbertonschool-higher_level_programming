#!/usr/bin/python3
"""
Method to check class
"""


def is_same_class(obj, a_class):
    """
    Method to check class
    Args:
        obj: object
        a_class: class
    Return:
        True or False
    """

    return all([type(obj) == a_class]) # return True or False
