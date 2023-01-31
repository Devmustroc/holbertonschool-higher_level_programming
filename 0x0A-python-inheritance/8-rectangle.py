#!/usr/bin/python3
"""
Class Module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Subclass"""
    def __init__(self, width, height): # initialization method
        """initialization method"""
        self.integer_validator('width', width) # validate width
        self.integer_validator('height', height) # validate height
        self.__width = width # set width
        self.__height = height # set height
