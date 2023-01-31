#!/usr/bin/python3
"""
class module
"""


class BaseGeometry():
    """Geometry class"""

    def area(self): # public instance method
        """raise exception is area not implemented"""
        raise Exception("area() is not implemented")  # raise exception

    def integer_validator(self, name, value): # public instance method
        """Checking if value is an int"""
        if type(value) != int: # if value is not an int
            raise TypeError(f"{name} must be an integer") # raise exception
        if value <= 0: # if value is less than or equal to 0
            raise ValueError(f"{name} must be greater than 0") # raise exception
