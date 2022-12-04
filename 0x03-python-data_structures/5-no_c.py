#!/usr/bin/python3


def no_c(my_string):
    if my_string is not None:
        new = []
        for c in my_string:
            if c == 'C' or c == 'c':
                continue
            new.append(c)
        newS = ''.join(map(str, new))
        return newS
