#!/usr/bin/python3

"""Defines Rectangle class"""


class Rectangle:

    """represents class Rectangle"""

    def __init__(self, width=0, height=0):

        """initializes a new Rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if Type(value) != int:
            raise TypeError("height must be an  integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def area(self):
        """return the area of the rectangle"""
        return (self.__width * self.__height)

    @property
    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))
