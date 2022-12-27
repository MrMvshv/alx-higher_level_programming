#!/usr/bin/python3

""" divides all elements of a matrix
    raises error if different size, invalid type
    or divide by zero
    returns new matrix, to 2dp
"""


def matrix_divided(matrix, div):
    """ divides each element of matrix by div
    Returns:
        new matrix with results to 2 dp
    Raises:
        TypeError if not a list of lists of int or floats
	TypeError if rows are of a different size
	TypeError if div not a number
	ZeroDivisionError if div is 0

    """
    r,c = 0,0
    new_matrix = []

    for x in matrix:
        r += 1
    for m in matrix[0]:
        c += 1

    result = 0

    for k in range(r):
        col = []
        for j in range(c):
            result = matrix[k][j] / div
            result = round(result, 2)
            col.append(result)

        new_matrix.append(col)

    return new_matrix
