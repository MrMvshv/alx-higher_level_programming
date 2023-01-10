#!/usr/bin/python3
""" isinstance function
    returns true or false
"""


def is_same_class(obj, a_class):
    """ returns True if is an instance
        otherwise false
    """
    if type(obj) == a_class:
        return True
    return False
