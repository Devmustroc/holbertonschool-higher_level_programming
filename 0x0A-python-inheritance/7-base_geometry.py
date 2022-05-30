#!/usr/bin/python3
"""
class module
"""


class BaseGeometry():
    """Geometry class"""

    def area(self):
        """raise exception is area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checking if value is an int"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        """Checking if value is not less than 0"""
        if value <= 0:
            raise TypeError(f"{name} must be greater than 0")
