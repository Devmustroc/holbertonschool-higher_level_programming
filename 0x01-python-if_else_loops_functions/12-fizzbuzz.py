#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101): # loop through the alphabet
        if i % 5 == 0 and i % 3 == 0:  # if the letter is e or q
            word = "FizzBuzz"  # skip the rest of the loop
        elif i % 5 == 0: # otherwise
            word = "Buzz" # print a string with a variable
        elif i % 3 == 0: # otherwise
            word = "Fizz" # print a string with a variable
        else: # otherwise
            word = str(i)
        print("{:s}".format(word), end=" ") # print a string with a variable

if __name__ == "__main__":
    fizzbuzz()
