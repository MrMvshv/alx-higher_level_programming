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
