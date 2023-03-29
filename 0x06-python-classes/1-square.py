#!/usr/bin/python3
# 1-square.py
""" Define a class Square. """


class Square():
    """ The class represent a Square.

        Attributes:
            attr1(int): this is a private field
    """
    def __init__(self, size):
        """ The method run as  an object of class is instantiated

            Args:
                size(int): size of the square which is private
            Return:
                size of the square
        """
        self.__size = size
