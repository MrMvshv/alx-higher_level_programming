#!/usr/bin/python3
""" class definition
    called base geometry
    with dummy function area
    and integer validator
"""


class BaseGeometry:
    """ is a  class definition
        contains area function
    """
    def area(self):
        """ area function
            raises exception
        """
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """ integer validator
            raisws typeerror or valueerror
	    if not int or <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
