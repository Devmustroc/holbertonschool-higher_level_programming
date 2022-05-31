#!/usr/bin/python3
"""File name : 2-append_write.py"""


def append_write(filename="", text=""):
    """append_write appends a string
    at the end of a text file (UTF8)

    Args:
        filename(str): default.
        text(str): text to add. Default
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
