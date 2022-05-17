#!/usr/bin/python3
"""
defined class definition
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
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """size: size of the square
        setter validating size is int and >= 0

        Raise:
             TypeError and ValueError
        """
        return (self.__size)

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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns: Area of a Square instance
        """
        return (self.size**2)

    def my_print(self):
        """
        prints in stdout the square with the character # or a new line
        is size is zero.
        """
        if self.__size == 0:
            print()
        for col in range(self.__size):
            for row in range(self.__size):
                print("#", end="")
            print()
