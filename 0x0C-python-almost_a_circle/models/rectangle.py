#!/usr/bin/python3

""" class rectangle definition
    inherits from Base
    width,height,x,y as private instance attributes
    getter and setter defined
    constructor defined
"""
from models.base import Base

class Rectangle(Base):
    """ rectangle with width and height properties
        Attributes:
        width(int), height(int), x, y
        initialization with default value of 0 for both
    """
    def valid8(var, varType):
        """ validates a variable
            checks > 0 and int
        """
        if type(var) != int:
            raise TypeError("{} must be an integer".format(varType))
        elif var <= 0:
            raise ValueError("{} must be > 0".format(varType))

    def valid82(var, varType):
        """ validates a variable
            checks > 0 and int
        """
        if not isinstance(var, int):
            raise TypeError("{} must be an integer".format(varType))
        elif var < 0:
            raise ValueError("{} must be >= 0".format(varType))

    def __init__(self, width, height, x=0, y=0, id=None):
        """ uses super's logic
            assign width, height, x, y
        """
        Rectangle.valid8(width, "width")
        Rectangle.valid8(height, "height")
        Rectangle.valid82(x, "x")
        Rectangle.valid82(y, "y")

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        Rectangle.valid8(height, "height")
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        Rectangle.valid8(width, "width")
        self.__width = width

    @property
    def x(self):
        """ Get/set x of rectangle """
        return self.__x

    @x.setter
    def x(self, x):
        Rectangle.valid82(x, "x")
        self.__x = x

    @property
    def y(self):
        """ Get/set y of rectangle """
        return self.__y

    @y.setter
    def y(self, y):
        Rectangle.valid82(y, "y")
        self.__y = y

    def area(self):
        """ return area
            of rectangle instance
        """
        return (self.__width * self.__height)

    def display(self):
        """ display rectangle using #
            skips y lines
            and x spaces before printing
            character in stdout
        """
        for m in range(self.__y):
            print()
    
        for y in range(self.__height):
            for j in range (self.__x):
                print(" ", end='')
            for x in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,\
        self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns arguments to each attribute
            args: id, width, height, x, y
        """
        if len(args) > 0:
            y = 0
            for x in args:
                y += 1
                if y == 1:
                    self.id = x
                elif y == 2:
                    self.width = x
                elif y == 3:
                    self.height = x
                elif y == 4:
                    self.x = x
                elif y == 5:
                    self.y = x
                else:
                    break
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation
           of a rectangle
        """
        rect_dict = {'x': self.x, 'y': self.y,\
        'id': self.id, 'height': self.height, 'width': self.width}
        return rect_dict
