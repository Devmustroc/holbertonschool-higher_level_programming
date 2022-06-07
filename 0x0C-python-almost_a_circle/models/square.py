#!/usr/bin/python3
"""Module that contains class Square inheritance
from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize instance of Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method"""
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_square + str_id + str_xy + str_wh

    @property
    def size(self):
        """Getter Size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        if isinstance(value, int):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise ValueError("width must be an integer")

    def __str__(self):
        """str special method"""
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_rectangle + str_id + str_xy + str_size

    def update(self, *args, **kwargs):
        """Update Method"""
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', ' x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionself._Rectangle__yary representation of a Rectangle"""
        return {'id': self.id, "y": self._Rectangle__y, "x": self.Rectangle__x, 'size': self.size}
