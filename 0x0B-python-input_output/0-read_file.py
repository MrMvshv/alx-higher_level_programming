#!/usr/bin/python3
""" read_file reads a file
    then prints it to stdout
"""
def read_file(filename=""):
    """ reads a file
        then prints it efficiently
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='') 
