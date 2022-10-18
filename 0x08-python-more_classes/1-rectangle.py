#!/usr/bin/python3

""" insert module to define a rectangle"""


class Rectangle:
    def __init__(self, height=0, width=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """method to get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            return self.__width = value

    @property
    def height(self):
        """method to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):

        """method to set value of height"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            return self.__height = value
