#!/usr/bin/python3
# 6-square.py
"""Define a class Square. """


class Square():
    """Represents a square

       Attributes:
           attr1(int): this is size of the square

    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize when created

           Args:
               size(int): a private field
               postion
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter method for size

           Args:
               __size(int): the size to get
           Return:
               the set size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Setter method for size

            Args:
                value(int): the value to set to size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    @property
    def position(self):
        """ Getter method for position

            Args:
                __position(int, int):tuple of two integers

            Return:
                positions
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Setter method for position

            Args:
                value(int, int): a tuple of two integers
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__postion = value

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
            print(" ")
            return
        else:
            [print(" ", end="") for i in range(0, self.__position[1])
             if not self.__position[1] > 0]
            for i in range(self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                print("#" * self.__size)
