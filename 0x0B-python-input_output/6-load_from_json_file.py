#!/usr/bin/python3
""" creates an object from a file
    using json representation
"""
import json


def load_from_json_file(filename):
    """ loads object
        from json file
        no exceptions
        returns json of file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f.read())
