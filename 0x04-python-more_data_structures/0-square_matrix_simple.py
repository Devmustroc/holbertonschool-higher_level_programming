#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return [list(map(lambda j: j**2, item)) for item in matrix]
