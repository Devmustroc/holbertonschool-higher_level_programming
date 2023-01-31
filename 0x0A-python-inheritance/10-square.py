#!/usr/bin/python3
"""
Class Square Module
"""
Rectangle = __import__('9-rectangle').Rectangle # import Rectangle class


class Square(Rectangle): # Square
    """class inherits from Rectangle"""

    def __init__(self, size): # initialization method
        """initialization method"""
        self.integer_validator("size", size) # validate size
        self.__size = size # set size
        super().__init__(self.__size, self.__size) # call super class
