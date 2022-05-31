#!/usr/bin/python3
""" File name : 4-from_json_string.py"""
import json


def from_json_string(my_str):
    """from_json_string  returns an object
    (python data struct) respresented by a JSON string

    Args:
    my_obj (obj): anything object e.g: list dict
    """
    return(json.loads(my_str))
