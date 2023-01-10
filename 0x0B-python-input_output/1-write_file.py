#!/usr/bin/python3
""" writes a string to a file
    returns no of chars written
    creates or overwrites
"""


def write_file(filename="", text=""):
    """ writes a new file
        overwrites if existing
        returns no. of chars written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
