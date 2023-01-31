#!/usr/bin/python3
def print_last_digit(number):  # define a function
    if number < 0: # if the number is less than 0
        final = ((number * -1) % 10)  # assign a value to a variable
    elif number > 0:  # if the number is greater than 0
        final = number % 10  # assign a value to a variable
    else:  # if the number is equal to 0
        final = number  # assign a value to a variable
    print("{:d}".format(final), end="")  # print a string with a variable
    return final  # return a value
