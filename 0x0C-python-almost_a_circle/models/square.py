#!/usr/bin/python3
"""
Module that contains class Square,
inheritance of class Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Module that contains class Square,
    inheritance of class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Class Square that defines a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        str special method
        """
        return f'[Square] {self.id} {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """ Getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """ Returns a dictionary with attributes """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
