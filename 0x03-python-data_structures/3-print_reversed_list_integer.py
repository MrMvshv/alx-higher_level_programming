#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    x = len(my_list) - 1
    if x <= 0:
        return
    while x >= 0:
        print("{:d}".format(my_list[x]))
        x = x - 1


if __name__ == '__main__':
    print_list_integer([])
