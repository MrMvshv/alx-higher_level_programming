#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    j = len(matrix) - 1
    k = len(matrix[0]) - 1
    for x in matrix:
        for m in x:
            print("{:d}".format(m), end='')
            if m == x[k]:
                print("", end='\n')
            else:
                print("", end=' ')
    print("", end='\n')
