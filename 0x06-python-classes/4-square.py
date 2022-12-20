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
        """ area gets area
            returns: area
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ size getter
            returns size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter
            set value with error catching
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
