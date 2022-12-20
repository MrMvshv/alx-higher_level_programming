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
            Args:
                size: of square
            Raises:
                TypeError: not int
                ValueError: < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return (self.__size ** 2)
