#!/usr/bin/python3
"""Class Rectangle inhenerit from Base Class Module"""

from models.base import Base


class Rectangle(Base):
    """Class rectangle that defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """intializing instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter and Setter for Width"""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Getter and Setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def x(self):
        """Getter and Setter for argement x"""
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """Getter & setter for argement y"""
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, int):
            self.__y = value
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """return the area Value of the Rectangle instance"""
        return self.width * self.__height

    def display(self):
        """Display in Standart output the rectangle instance with caracter #"""
        for row in range(self.y):
            print("")
        for col in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for k in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """str special method"""
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_yx = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_yx + str_wh

    def update(self, *args, **kwargs):
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {"x": self.__x, "y": self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
