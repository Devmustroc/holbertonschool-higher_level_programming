#!/usr/bin/python3
""" 0-main """
from models.base import Base # import class Base

if __name__ == "__main__":  # if the file is executed as the main program

    b1 = Base()  # create an instance of class Base
    print(b1.id)

    b2 = Base()  # create an instance of class Base
    print(b2.id)

    b3 = Base() # create an instance of class Base
    print(b3.id)

    b4 = Base(12) # create an instance of class Base
    print(b4.id)

    b5 = Base() # create an instance of class Base
    print(b5.id)
