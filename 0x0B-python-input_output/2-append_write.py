#!/usr/bin/python3
"""
2-append_write.py
append_write(filename="", text="")
"""


def append_write(filename="", text=""): #
    """append_write(filename="", text="")
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """

    with open(filename, 'a', encoding='utf-8') as f: # open file in append mode
        return f.write(text) # write text to file and return number of characters written
