#!/usr/bin/python3
"""
define square class
"""


class Square():
    """
    private instance attribute class size
    """

    def __init__(self, size=0):
        """
        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
