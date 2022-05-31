#!/usr/bin/python3
""" File name : 6-load_from_json_file.py"""


def load_from_json_file(filename):
    """Crate an Object from a 'JSON file' and return it"""
    import json
    with open(filename, 'r') as f:
        return json.load(f)
    
