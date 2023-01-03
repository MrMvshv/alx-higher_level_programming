#!/usr/bin/python3

""" prints a text with 2 new lines after
    '.' , '?' and ':'
    text must be string
"""


def text_indentation(text):
    m = 0

    if not isinstance(text, str):
            raise TypeError("text must be a string")
    for x in text:
        if m == 1:
            m = 0
            if x != ' ':
                print("{}".format(x), end='')
        elif x == '.' or x == ':' or x == '?':
            print("{}".format(x))
            print()
            m = 1
        else:
            print("{}".format(x), end='')
