#!/usr/bin/python3

"""Defines a classs Rectangle"""


class Rectangle:

    """represents Rectangle class"""

    def __init__(self, width=0, height=0):

        """initializes a new rectangle"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """gets the value of width"""

        return self.__width
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets and sets the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def area(self):
        """return the area of the rectangle"""
        return (self.__height * self.__width)

    @property
    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    
    def __str__(self):
        """returns the printable representation of the rectangle with character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")

        return ("".join(rect))







