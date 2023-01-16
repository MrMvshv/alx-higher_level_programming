#!/usr/bin/python3
""" class square definition
    inherits from Rectangle
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """ square is a rectangle
        whose width = height
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ inits using rectangle logic """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ overrides by printing square
            instead
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,\
        self.x, self.y, self.width)

    @property
    def size(self):
        """ Get/set x of rectangle """
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

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
                    self.size = x
                elif y == 3:
                    self.x = x
                elif y == 4:
                    self.y = x
                else:
                    break
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation
           of a square
        """
        sq_dict = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return sq_dict
