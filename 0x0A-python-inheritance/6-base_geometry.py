#!/usr/bin/python3
"""
class module
"""


class BaseGeometry():
    """Geometry class"""
    def area(self): # public instance method
        """raise exception is area is not implemented"""
        raise Exception("area() is not implemented") # raise exception
