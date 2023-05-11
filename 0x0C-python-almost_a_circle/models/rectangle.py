#!/usr/bin/python3
"""This representing a Rectangle"""
from models.base import Base
"""Superclass Base"""


class Rectangle(Base):
    """Define a class Rectangle and inherit from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instance of a class

           Args:
              width(int):representing the width
              height(int):representing the height
              x(int) = x
              y(int)= y
              id(int)= id inherited from the Base class
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width

           Return:
               width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the value for the width

           Args:
              value(int) = width

           Raise:
               TypeError
               ValueError
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height

           Return:
               height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """set value for height

           Args:
              value(int) = height

           Raise:
               TypeError
               ValueError
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x

           Return:
               x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """set value for x

           Args:
               value(int) = x

           Raise:
               TypeError
               ValueError
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y

           Return:
               y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """set y

           Args:
              value(int) = y

           Raise:
               TypeError
               ValueError
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """computes the area of every instance of a rectangle

           Return:
               width * height
        """
        return (self.__width * self.__height)

    def display(self):
        """ compute the area and print the character #"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """return a string

           Return:
               formatted string
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            __class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ methods update the Rectangle

            Args:
                *args = tuples
                **kwargs = dictionary
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
