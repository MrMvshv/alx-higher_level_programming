#!/usr/bin/python3

""" prints a # square
    whose size is given
    by the argument
"""


def print_square(size):
    """ prints a square
        using the #
        size must be an int
        and > 0
    """
    for x in range(size):
        for y in range(size):
            print("#", end='')
        print()
