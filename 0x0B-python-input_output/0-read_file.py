#!/usr/bin/python3
"""Module that contains a function that reads from a file"""


def read_file(filename=""):
    """Function that reads from a file
    args:   filename: name of the file to read from
    """


    with open(filename, 'r', encoding='utf-8') as f: # open file in read mode
        print(f.read(), end="") # read file and print to stdout
