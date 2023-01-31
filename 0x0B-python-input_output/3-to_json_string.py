#!/usr/bin/python3
""" File name : 3-to_json_string.py"""
import json     # import json module


def to_json_string(my_obj): # function to_json_string
    """to_json_string(my_obj)
    Returns the JSON representation of an object (string)
    args:
        my_obj: object to be converted to JSON
    """
    return(json.dumps(my_obj)) # return JSON representation of my_obj
