#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new = []
    i = 0
    for x in my_list:
        if x == search:
            print(x)
            new.append(replace)
        else:
            new.append(x)
    return new
