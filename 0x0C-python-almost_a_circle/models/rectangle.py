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
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        """
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
        """
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
        """
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
        """
        self.__y = value
