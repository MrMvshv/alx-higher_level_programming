#!/usr/bin/python3
""" returns object from json string
    representation of an object
"""
import json


def from_json_string(my_str):
    """ returns the object representation
        of a json (string):
        don’t need to manage exceptions
        if the string isn't an object
    """
    return json.loads(my_str)
