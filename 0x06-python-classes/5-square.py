#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        self.size = size

    def size(self):
        return(self.__size)

    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return(self.__size**2)

    def my_print(self):
        if self.__size is 0:
            print()

        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()