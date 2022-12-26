#!/usr/bin/python3
""" adds two integers and returns result
    raises error if not int or float
    returns result as int
"""

def add_integer(a, b=98):
    """ adds a and b
    Returns: integer result
    Raises: TypeError if not int or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
