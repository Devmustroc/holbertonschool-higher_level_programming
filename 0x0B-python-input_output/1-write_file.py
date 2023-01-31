#!/usr/bin/python3
"""file name : write_file.py"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8) and returns the
    number of characters written
    args:   filename: name of the file to write to
            text: string to write to the file
    """

    with open(filename, 'w', encoding='utf-8') as f: # open file in write mode
        return f.write(text) # write text to file and return number of chars
