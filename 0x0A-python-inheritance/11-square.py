#!/usr/bin/python3
""" class definition
    inherits from base geometry
    with private width and height
    using integer validator
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ is a  class definition
        contains initializer
    """
    def __init__(self, size):
        """ init function
            private variable size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ return string representation
            of the rectangle
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
