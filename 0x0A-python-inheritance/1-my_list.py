#!/usr/bin/python3
"""
This module has a class MyList that inherits from
list. has a public instance method print_print_sorted that
prints the list in ascending order
"""


class MyList(list):
    """
    Class that inherits from list
    """
    def print_sorted(self):
        print(sorted(self))
