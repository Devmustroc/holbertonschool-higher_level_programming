#!/usr/bin/python3
"""Module to print pascal triange"""


def pascal_triangle(n):
    """pascal_triangle

    Args:
        n (int): number
    Return:
    [List]: list of list of integeres representing
    a pascal triangle of number (n)->integer
    """
    if n <= 0:
        return("")

    triangle = [[1]]
    for current_row in range(1, n):
        row = [1]
        previous_row = triangle[current_row - 1]
        for element in range(1, current_row):
            row.append(previous_row[element] + previous_row[element - 1])
        row.append(1)
        triangle.append(row)
    return(triangle)
