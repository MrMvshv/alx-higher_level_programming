#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = [[]]
    if matrix is None or matrix == [[]]:
        return new
    new = []
    for y in matrix:
        new.append(list(map(lambda x: (x ** 2), y)))
    return new
