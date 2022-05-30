#!/usr/bin/python3
"""
class module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Geometry class"""
    def __init__(self, width, height):
        """initialization method"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Print Method"""
        return (f"[{__class__.__name__}] {self.__width}/{self.__height}")
