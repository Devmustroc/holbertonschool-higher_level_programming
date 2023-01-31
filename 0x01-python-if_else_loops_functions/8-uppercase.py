#!/usr/bin/python3
def uppercase(str): # function that prints a string in uppercase
    for i in str:  # loop through the alphabet
        change = 0  # variable to change the ascii value
        if ord(i) > 96 and ord(i) < 123:   # if the letter is lowercase
            change = 32   # change the ascii value
        print("{:s}".format(chr(ord(i) - change)), end="") # print a string with a variable
    print() # print a new line
