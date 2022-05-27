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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """size: size of the square
        setter validating size is int Square class definition
        setter validating size is int and >= 0
        Raise:
             TypeError and ValueError
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns area of the square instance
        """
        return (self.size ** 2)
