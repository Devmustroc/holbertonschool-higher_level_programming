#!/usr/bin/python3
for i in range(0, 8):  # loop through the alphabet
    for j in range(i + 1, 10):  # loop through the alphabet
        print("{:d}{:d}".format(i, j), end=", ")   # print a string with a variable
print("{:d}{:d}".format(i + 1, j))  # print a string with a variable
