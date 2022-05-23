#!/usr/bin/python3
"""
Rectangle Class
"""


class Rectangle:
    """class defined"""

    def __init__(self, width=0, height=0):
        """Initialization method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """function to return width if setter checks have passed"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter validates if value is >= 0
        Raises:
        TypeError
        ValueError
        """
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        if value < 0:
            raise TypeError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Setter Method of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Getter Method of height"""
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        if value < 0:
            raise TypeError('height must be >= 0')
        self.__height = value


class Rectangle:
    """
    This class has two attributes
    width
    height
    both will have property and setter function definition
    """

    def __init__(self, width=0, height=0):
        """
        instantiates width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        function to return width if setter checks have passed
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
        function to return height if setter checks have passed
        """
        return self.__height

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
        """Return area of width and height"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of width and height"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns string of Rectangle using #
        if 0 returns empty string"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for row in range(self.__height - 1):
            print("#" * self.__width)
        return ('#' * self.__width)

    def __repr__(self):
        """
        Returns a string
        """
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """
        when an instance of Rectangle is deleted
        Print bye message
        """
        print("Bye rectangle...")
