#!/usr/bin/python3
"""file name : write_file.py"""


def write_file(filename="", text=""):
    """write_file: write a string
    to a text file (utf-8)

    Args:
        filename(str): default.
        text(str): text to add. Default
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
