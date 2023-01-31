#!/usr/bin/python3
"""File name : 5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename): # function save_to_json_file
    """ save_to_json_file(my_obj, filename)
    Writes an Object to a text file, using a JSON representation
    args:
        my_obj: object to be converted to JSON
        filename: file to write JSON representation of my_obj
    """
    with open(filename, 'w', encoding='utf-8') as f:    # open file in write mode
        return(json.dump(my_obj, f))   # write JSON representation of my_obj to file