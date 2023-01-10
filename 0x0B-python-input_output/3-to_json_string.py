#!/usr/bin/python3
import json
""" returns json representation
    of an object
"""


def to_json_string(my_obj):
    """ returns the JSON representation
        of an object (string):
        don’t need to manage exceptions
        if the object can’t be serialized.
    """
    return json.dumps(my_obj)
