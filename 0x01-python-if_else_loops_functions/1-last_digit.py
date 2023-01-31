#!/usr/bin/python3
from lib2to3.pgen2.token import GREATER
import random
number = random.randint(-10000, 10000)   # assign a random value to a variable
greater = "and is greater than 5"      # assign a value to a variable
lesser = "and is less than 6 and not 0"     # assign a value to a variable
equal = "and is 0"    # assign a value to a variable

if number > 0: # if the number is greater than 0
    last = number % 10  # assign a value to a variable
else:  # if the number is less than 0
    last = ((number * -1) % 10) * -1    # assign a value to a variable

if last > 5:  # if the last digit is greater than 5
    final = greater  # assign a value to a variable
elif last == 0:     # if the last digit is equal to 0
    final = equal  # assign a value to a variable
elif last < 6 and not 0:  # if the last digit is less than 6 and not 0
    final = lesser  # assign a value to a variable
print("Last digit of", number, "is", last, final) # print a string with variables
