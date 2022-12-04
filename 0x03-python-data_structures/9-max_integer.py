#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    x = 0
    for m in my_list:
        if m > x:
            x = m
    return x
