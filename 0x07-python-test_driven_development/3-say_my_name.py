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
    print("My name is {} {}".format(first_name,last_name))
