#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    x = len(my_list) - 1
    if x < 0 or my_list is None:
        return
    while x >= 0:
        print("{:d}".format(my_list[x]))
        x = x - 1
