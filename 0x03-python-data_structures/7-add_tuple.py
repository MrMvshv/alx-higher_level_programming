#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        a, b = tuple_a[0], tuple_a[1]
    elif len(tuple_a) == 0:
        a, b = 0, 0
    else:
        a, b = tuple_a[0], 0
    if len(tuple_b) >= 2:
        c, d = tuple_b[0], tuple_b[1]
    elif len(tuple_b) == 0:
        c, d = 0, 0
    else:
        c, d = tuple_b[0], 0

    tuple_c = (a + c, b + d)
    return tuple_c


if __name__ == '__main__':
    add_tuple(tuple_a=(), tuple_b=())
