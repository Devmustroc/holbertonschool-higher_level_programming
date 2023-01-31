#!/usr/bin/python3
"""Module to print pascal triange"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    args:
        n: number of rows
    return:
        list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0: # if n is less than or equal to 0
        return("") # return empty string

    triangle = [[1]] # create list of lists of integers
    for current_row in range(1, n): # iterate through rows
        row = [1] # create row
        previous_row = triangle[current_row - 1] # set previous row
        for element in range(1, current_row): # iterate through elements
            row.append(previous_row[element] + previous_row[element - 1]) # append element to row
        row.append(1) # append 1 to row
        triangle.append(row) # append row to triangle
    return(triangle) # return triangle
