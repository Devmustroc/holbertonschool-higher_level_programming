#!/usr/bin/python3
"""
Rectangle Class
"""


class Rectangle:
    """Class of Rectangle"""

    def __init__(self, width=0, height=0):
        """
        instantiates width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        function to return width if
        setter checks have passed
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter validates if value is >= 0
        Raises:
        TypeError
        ValueError
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        function to return height if
        setter checks have passed
        """
        return (self.width * self.height)

    @height.setter
    def height(self, value):
        """
        setter validates if value is >= 0
        Raises:
        TypeError
        ValueError
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method to return area of width and height"""
        return self.__width * self.__height

    def perimeter(self):
        """method to return perimeter of width and height"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """method string object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for row in range(self.__height - 1):
            print("#" * self.__width)
        return ('#' * self.__width)

    def __repr__(self):
        """repr method"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        Prints when deleting an instance
        """
        print("Bye rectangle...")
