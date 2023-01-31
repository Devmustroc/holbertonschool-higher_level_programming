#!/usr/bin/python3
"""
Module that contains class Square,
inheritance of class Rectangle
"""

from models.rectangle import Rectangle # import class Rectangle


class Square(Rectangle): # class Square that inherits from class Rectangle
    """
    Module that contains class Square,
    inheritance of class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None): # constructor method
        """Class Square that defines a square"""
        super().__init__(size, size, x, y, id)  # call the super class with id

    def __str__(self): # str special method
        """
        str special method
        """
        return f'[Square] {self.id} {self.x}/{self.y} - {self.width}' # return a string

    @property # decorator
    def size(self): # size getter
        """ Getter size """
        return self.width   # return the private instance attribute

    @size.setter  # decorator
    def size(self, value):  # size setter
        """ Setter size """
        self.width = value  # assign the private instance attribute
        self.height = value  # assign the private instance attribute

    def update(self, *args, **kwargs):  # update method
        """ update method """
        argc = len(args)  # number of arguments
        kwargc = len(kwargs)  # number of keyword arguments
        modif_attrs = ['id', 'size', 'x', 'y']  # list of attributes

        if argc > 4:  # if argc is greater than 4
            argc = 4    # argc is equal to 4

        if argc > 0:  # if argc is greater than 0
            for i in range(argc):  # for i in range of argc
                setattr(self, modif_attrs[i], args[i])  # set the attribute
        elif kwargc > 0:  # if kwargc is greater than 0
            for k, v in kwargs.items():  # for key, value in kwargs.items()
                if k in modif_attrs:  # if key is in modif_attrs
                    setattr(self, k, v)  # set the attribute

    def to_dictionary(self):  # method that returns the dictionary representation of a Square
        """ Returns a dictionary with attributes """
        return {
            'id': self.id,  # return a dictionary
            'size': self.size,  # return a dictionary
            'x': self.x,  # return a dictionary
            'y': self.y  # return a dictionary
        }  # return a dictionary
