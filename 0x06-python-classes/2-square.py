#!/usr/bin/python3


""" class square definition
    optional size, error checking
    size
"""


class Square:
    """ square class
        Attributes:
           size(int): size of sq
    """
    def __init__(self, size=0):
        """ initialize square
            to size
        """
        try:
            size / 1
            if size < 0:
                raise ValueError
            else:
                self.__size = size
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
