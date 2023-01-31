#!/usr/bin/python3
def islower(c):  # function that checks for lowercase character
    if ord(c) >= 97 and ord(c) <= 123:  # if the character is lowercase
        return True   # return True
    else:           # otherwise
        return False  # return False
