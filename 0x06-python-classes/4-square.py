#!/usr/bin/python3
"""Square class file"""


class Square():
    """
    Square class with private instance attribute size
    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        size: size of the square
        setter validating size is int and >= 0

        Raise: TypeError, ValueError
        """
        return(self.__size)

    @size.setter
    def size(self, value):
        """size: size of the square
        setter validating size is int and >= 0

        Raises:
            TypeError: exception
            ValueError: exception
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value > 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return area of the square instance
        """
        return(self.size**2)
