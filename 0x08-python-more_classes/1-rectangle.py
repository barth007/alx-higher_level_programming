#!/usr/bin/python3
# 1-rectangle.py
""" Define a Rectangle """


class Rectangle:
    """ Represent a Rectangle

        Attributes:
            attr1(int):The width of the rectangle
            attr2(int): The height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize when created

           Args:
               width(int): private field of the rectangle width
               height(int):private field of the rectangle height
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Getter method for width

           Args:
               __width(int): The width of the rectangle
           Return:
               the set width
        """
        return (self.__width)

    @property
    def height(self):
        """Getter method for height

           Args:
               __height(int):The height of the rectangle
           Return:
               The set height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter method for height

           Args:
               value(int):The value that will be assign to height
           Return:
               The set height = value
           Raise:
               TypeErro and ValueError
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        """Setter method for width

           Args:
               value(int): The value that will be assign to width
           Return:
               The set width = value
           Raise:
               TypeError and ValueError
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= ")
        else:
            self.__width = value
