#!/usr/bin/python3
# 2-square.py
"""Define a Class Square"""


class Square():
    """Represents a class Square

       Attributes:
           attr1(int): This a private field of an integer data type
    """

    def __init__(self, size=0):
        """Initialize a new instance

           Args:
               size(int): A size of a square
           """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
