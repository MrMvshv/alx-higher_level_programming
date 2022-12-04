#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if len(matrix) != 0:
        j = len(matrix)
        k = len(matrix[0])
        for x in range(j):
            for m in range(k):
                print("{:d}".format(matrix[x][m]), end='')
                if m == k - 1:
                    print("", end='\n')
                else:
                    print("", end=' ')
    else:
        print()
