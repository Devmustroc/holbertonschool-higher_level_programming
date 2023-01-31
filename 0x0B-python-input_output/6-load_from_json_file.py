#!/usr/bin/python3
""" File name : 6-load_from_json_file.py"""
import json    # import json module

def load_from_json_file(filename):
    """Crate an Object from a 'JSON file' and return it
    args:
        filename: file to be read
    """

    with open(filename, 'r') as f: # open file in read mode
        return(json.load(f)) # return object represented by JSON in file
