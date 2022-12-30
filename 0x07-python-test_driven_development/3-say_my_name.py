#!/usr/bin/python3

""" prints a name
    prints my name is
    then the first, last name
"""


def say_my_name(first_name, last_name=""):
    """ prints both names
    Raises:
        TypeError if not strings
    """
    typeErr = 0
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name,last_name))
