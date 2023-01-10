#!/usr/bin/python3
""" writes an object to a file
    using json representation
    creates or overwrites
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes a new file
        overwrites if existing
        returns no. of chars written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
