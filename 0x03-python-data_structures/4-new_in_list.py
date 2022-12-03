#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    b = []
    for x in my_list:
        b.append(x)
    b[idx] = element
    return b


if __name__ == '__main__':
    print_list_integer([])
