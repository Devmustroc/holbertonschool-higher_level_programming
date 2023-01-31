#!/usr/bin/python3
"""
class module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry # import class


class Rectangle(BaseGeometry): # Rectangle subclass
    """Geometry class"""
    def __init__(self, width, height): # initialization method
        """initialization method"""
        self.integer_validator('width', width) # validate width
        self.integer_validator('height', height)     # validate height
        self.__width = width # set width
        self.__height = height # set height

    def area(self): # public instance method
        """calculate the area of a rectangle"""
        return self.__width * self.__height # return area

    def __str__(self): # print method
        """Print Method"""
        return (f"[{__class__.__name__}] {self.__width}/{self.__height}")   # return string
