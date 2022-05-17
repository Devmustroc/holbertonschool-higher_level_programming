#!/usr/bon/python3
"""define class square"""


class Square():
    """
        Square class with private instance attribute size
    """
    def __init__(self, size=0):
        """

        Args:
            size : size of the square

        Raises:
            TypeError: exception
            ValueError: exception
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            Return Area of a Square Instance
        """
        return (self.__size**2)
