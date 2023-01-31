#!/usr/bin/python3
import random # import the random module
number = random.randint(-10, 10) # assign a random value to a variable
if number > 0: # if the number is greater than 0
    print(number, "is positive") # print a string with a variable
elif number < 0: # if the number is less than 0
    print(number, "is negative") # print a string with a variable
else: # if the number is equal to 0
    print(number, "is zero") # print a string with a variable
