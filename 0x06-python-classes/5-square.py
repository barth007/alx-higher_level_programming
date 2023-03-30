#!/usr/bin/python3
# 5-square.py
"""Define a class Square. """


class Square():
    """Represents a square

       Attributes:
           attr1(int): this is size of the square

    """
    def __init__(self, size=0):
        """initialize when created

           Args:
               size(int): a private field
        """
        self.__size = size

    @property
    def size(self):
        """Getter method

           Args:
               __size(int): the size to get
           Return:
               the set size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Setter method

            Args:
                value(int): the value to set to size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """method calculate the area of square

           Args:
               __size(int): the value

           Return:
               area of the square is returned
           """
        return (self.__size ** 2)

    def my_print(self):
        """method prints a character according to the area

           Args:
               __size(int): the size of the square which is a private
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
