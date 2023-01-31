#!/usr/bin/python3
""" File name : 4-from_json_string.py"""
import json


def from_json_string(my_str):
    """from_json_string(my_str)
    Returns an object (Python data structure) represented by a JSON string
    args:
        my_str: JSON string to be converted to object
    """
    return(json.loads(my_str)) # return object represented by my_str
