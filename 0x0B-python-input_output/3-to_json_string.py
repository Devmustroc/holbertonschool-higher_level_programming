#!/usr/bin/python3
""" File name : 5-to_json_string.py"""


def to_json_string(my_obj):
    """to_json_string  returns the JSON
    representation of an object (string)

    Args:
    my_obj (obj): anything object e.g: list dict
    """
    return(json.dumps(my_obj))
