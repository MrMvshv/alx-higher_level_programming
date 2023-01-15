#!/usr/bin/python3
""" first class Base
    with private class attribute __nb_objects
    public instance attribute id
"""


class Base:
    """ public instance attribute id
        private class attribute __nb_objects
        The goal of it is to manage id attribute
        in all your future classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ base initializer
            init id to id if id != None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
