#!/usr/bin/python3
""" class Rectangle, inheritance of class Base"""

from models.base import Base # import class Base

class Rectangle(Base): # class Rectangle that inherits from class Base
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):   # constructor method
        """ Constructor method """
        super().__init__(id)    # call the super class with id - super() with no arguments returns a proxy object
        # that allows you to refer parent class by 'super'.

        self.check_integer_parameter(width, 'width') # check if width is an integer
        self.check_integer_parameter(height, 'height')  # check if height is an integer
        self.check_integer_parameter(x, 'x')   # check if x is an integer
        self.check_integer_parameter(y, 'y')  # check if y is an integer

        self.__width = width   # assign the private instance attribute
        self.__height = height # assign the private instance attribute
        self.__x = x  # assign the private instance attribute
        self.__y = y # assign the private instance attribute

    @property # decorator
    def width(self): # width getter
        """ width getter """
        return self.__width # return the private instance attribute

    @width.setter # decorator
    def width(self, param): # width setter
        """heigh setter"""
        self.check_integer_parameter(param, 'width') # check if param is an integer

        self.__width = param # assign the private instance attribute

    @property # decorator
    def height(self): # height getter
        """getter height"""
        return self.__height # return the private instance attribute

    @height.setter # decorator
    def height(self, param): # height setter
        """setter height"""
        self.check_integer_parameter(param, 'height') # check if param is an integer

        self.__height = param # assign the private instance attribute

    @property # decorator
    def x(self): # x getter
        """ x getter """
        return self.__x # return the private instance attribute

    @x.setter # decorator
    def x(self, param): # x setter
        """ x setter """
        self.check_integer_parameter(param, 'x')

        self.__x = param # assign the private instance attribute

    @property # decorator
    def y(self): # y getter
        """ y getter """
        return self.__y # return the private instance attribute

    @y.setter # decorator
    def y(self, param): # y setter
        """ y setter """
        self.check_integer_parameter(param, 'y')  # check if param is an integer

        self.__y = param # assign the private instance attribute

    def check_integer_parameter(self, value, param):  # check if value is an integer
        """check integer parametre"""
        if type(value) is not int: # if value is not an integer
            raise TypeError(param + ' must be an integer')  # raise an error

        if value <= 0 and param in ('width', 'height'):  # if value is less than or equal to 0 and param is width or height
            raise ValueError(param + ' must be > 0')  # raise an error

        if value < 0 and param in ('x', 'y'): # if value is less than 0 and param is x or y
            raise ValueError(param + ' must be >= 0')  # raise an error

    def area(self): # method that returns the area of the rectangle
        """ returns the area of the rectangle object """
        return self.__width * self.__height  # return the area

    def display(self): # method that prints in stdout the Rectangle instance with the character #
        """ displays a rectangle """
        if self.__y > 0: # if y is greater than 0
            print('\n' * self.__y, end='')  # print a new line

        for i in range(self.height): # for i in range of height
            if self.__x > 0: # if x is greater than 0
                print(' ' * self.__x, end='')   # print a space

            print('#' * self.__width) # print a #

    def __str__(self): # str special method
        """ str special method """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )   # return a string

    def update(self, *args, **kwargs): # method that assigns an argument to each attribute
        """ update method """
        argc = len(args) # number of arguments
        kwargc = len(kwargs) # number of keyword arguments
        modif_attrs = ['id', 'width', 'height', 'x', 'y'] # list of attributes

        if argc > 5: # if argc is greater than 5
            argc = 5 # argc is 5

        if argc > 0: # if argc is greater than 0
            for i in range(argc): # for i in range of argc
                setattr(self, modif_attrs[i], args[i]) # set the attribute
        elif kwargc > 0:
            for k, v in kwargs.items(): # for key, value in kwargs.items()
                if k in modif_attrs: # if key is in modif_attrs
                    setattr(self, k, v) # set the attribute

    def to_dictionary(self):  # method that returns the dictionary representation of a Rectangle
        """ method that returs a dictionary with properties """
        return {
            'id': self.id,  # return a dictionary
            'width': self.width,    # return a dictionary
            'height': self.height,  # return a dictionary
            'x': self.x,  # return a dictionary
            'y': self.y  # return a dictionary
        }
