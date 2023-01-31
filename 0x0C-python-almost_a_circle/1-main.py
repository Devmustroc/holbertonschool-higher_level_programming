#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2) # create an instance of class Rectangle
    print(r1.id)

    r2 = Rectangle(2, 10)   # create an instance of class Rectangle
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)  # create an instance of class Rectangle
    print(r3.id)
