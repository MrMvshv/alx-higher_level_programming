#!/usr/bin/python3
""" class definition
    inherits from base geometry
    with private width and height
    using integer validator
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ is a  class definition
        contains initializer
    """
    def __init__(self, width, height):
        """ init function
            private variables
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area function
            returns area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """ return string representation
            of the rectangle
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
