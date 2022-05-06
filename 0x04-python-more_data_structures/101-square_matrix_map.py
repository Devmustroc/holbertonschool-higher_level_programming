#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_M = [[elem**2 for elem in row] for row in matrix]
    return new_M
