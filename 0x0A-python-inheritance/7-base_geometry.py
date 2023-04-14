#!/usr/bin/python3
# 6-base_geometry.py
""" Representation of a BaseGeometry """


class BaseGeometry:
    """ Defines a BaseGeometry"""

    def area(self):
        """ computes an ara

            Return:
                coomputed area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate an integer

            Args:
                name(string)
                value(int)
            Raise:
                TypeError
                ValueError
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
