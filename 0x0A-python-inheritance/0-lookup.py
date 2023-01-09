#!/usr/bin/python3
""" lookup function
    looks up a class
"""


def lookup(obj):
    """ returns the list of available
        attributes and methods
        of an object
    """
    return (dir(obj))
