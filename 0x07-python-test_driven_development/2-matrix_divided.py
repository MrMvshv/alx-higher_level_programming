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
    r,c,p = 0,0,0
    new_matrix = []

    for x in matrix:
        r += 1
        c = 0
        for m in x:
            print("{}:m".format(m))
            if not isinstance(m, (int, float)):
                r = 1
                break
            c += 1
    for x in matrix:
        if r == 1:
            break
        p = 0
        for m in x:
            p += 1
        print("{}:r, {}:p, {}:c".format(r,p,c))
        if p != c:
            p = 0
            break

    print("{}:r, {}:p".format(r,p))
    if r == 1:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif p == 0:
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    result = 0

    for k in range(r):
        col = []
        for j in range(c):
            result = matrix[k][j] / div
            result = round(result, 2)
            col.append(result)

        new_matrix.append(col)

    return new_matrix
