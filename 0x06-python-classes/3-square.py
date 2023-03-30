#!/usr/bin/python3
# 3-square.py
"""Define a class Square"""


class Square:
    """Represent a square

       Attributes:
           attr1(int): size of the square
   """
    def __init__(self, size=0):
        """initializing a new square

           Args:
               size(int): size of the square which will be a private
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculating area of a square

           Args:
               __size(int):a private field which is the size of the square

          Return:
              calculated area of the square
        """
        return self.__size * self.__size
