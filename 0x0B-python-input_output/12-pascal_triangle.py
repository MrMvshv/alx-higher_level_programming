#!/usr/bin/python3
""" list of lists of integers 
    representing the Pascal’s triangle of n
    empty list if n <= 0
"""
def pascal_triangle(n):
    """ returns a list of lists of integers 
        representing the Pascal's triangle of n
	Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    nw = []
    nx = []
    for x in range(n):
        if x == 0:
            nx = [1]
        elif x == 1:
            nx = [1, 1]
        else:
            tmp = []
            y = 0
            tmp.append(1)
            for y in range(x - 1):
                tmp.append(nx[y] + nx[y + 1])
            tmp.append(1)
            nx = tmp[:]    
        nw.append(nx)
    return nw
