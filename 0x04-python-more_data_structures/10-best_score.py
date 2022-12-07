#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    m = 0
    key = None
    keys = list(a_dictionary)
    for y in keys:
        if a_dictionary[y] > m:
            m = a_dictionary[y]
            key = y
        else:
            continue
    return key
