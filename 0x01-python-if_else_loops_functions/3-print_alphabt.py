#!/usr/bin/python3
for i in range(97, 123):    # loop through the alphabet
    if chr(i) == 'e' or chr(i) == 'q': # if the letter is e or q
        continue   # skip the rest of the loop
    else:         # otherwise
        print("{:s}".format(chr(i)), end="") # print a string with a variable
