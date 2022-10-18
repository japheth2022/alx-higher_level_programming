#!usr/bin/python3

""" insert module to define a real rectangle"""


class Rectangle:

    """class rectangle with private instance attribute width and height"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """method to get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):

        """method to set width value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):

        """method to retrieve height"""

        return self.__height

    @height.setter
    def height(self, value):

        """method to set value of height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
