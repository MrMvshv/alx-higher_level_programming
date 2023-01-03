#!/usr/bin/python3

""" class rectangle definition
    width and height included as private instance attributes
    getter and setter defined
"""


class Rectangle:
    """ rectangle with width and height properties
        Attributes:
            width(int), height(int)
        initialization with default value of 0 for both
    """
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    def area(self):
        """ returns area of rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """ returns self as string
        """
        str1 = ""

        if self.__width == 0 or self.__height == 0:
            return str1
        for y in range(self.__height):
            for x in range(self.__width):
                str1 += "#"
            if (y != (self.__height - 1)):
                str1 += "\n"
        return str1
