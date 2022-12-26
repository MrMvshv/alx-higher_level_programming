#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for i in sorted(list(a_dictionary)):
        print(i, end=': ')
        print(a_dictionary[i])
