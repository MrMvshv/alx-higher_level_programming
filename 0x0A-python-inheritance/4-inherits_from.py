#!/usr/bin/python3
""" is inherited from class function
    returns true or false
"""


def inherits_from(obj, a_class):
    """ returns True if is an inherited class
        otherwise false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
