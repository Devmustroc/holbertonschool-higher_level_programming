#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__": # if the file is executed as the main program

    try: # try to execute the following code
        Rectangle(10, "2") # create an instance of class Rectangle
    except Exception as e: # if an exception is raised
        print("[{}] {}".format(e.__class__.__name__, e)) # print the exception

    try: # try to execute the following code
        r = Rectangle(10, 2)  # create an instance of class Rectangle
        r.width = -10  # assign the private instance attribute
    except Exception as e:  # if an exception is raised
        print("[{}] {}".format(e.__class__.__name__, e))  # print the exception

    try:  # try to execute the following code
        r = Rectangle(10, 2)  # create an instance of class Rectangle
        r.x = {}  # assign the private instance attribute
    except Exception as e:  # if an exception is raised
        print("[{}] {}".format(e.__class__.__name__, e))  # print the exception

    try:  # try to execute the following code
        Rectangle(10, 2, 3, -1)  # create an instance of class Rectangle
    except Exception as e:  # if an exception is raised
        print("[{}] {}".format(e.__class__.__name__, e))  # print the exception
