#!/usr/bin/python3
""" writes a string to a file
    returns no of chars written
    creates or overwrites
"""


def append_write(filename="", text=""):
    """ writes a new file
        overwrites if existing
        returns no. of chars written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
