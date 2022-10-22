#!/usr/bin/python3
"""defines arectangle"""


class Rectangle:

    """represents a rectangle"""

    def __init__(self, width=0, height=0)

    """initializes a new rectangle.

    args:
        width(int): width of the  rectangle
        height(int): height of the rectangle

    """
    self.width = width
    self.height = height

    @property
    def width(self) -> int:

        """method to get value of width"""

        return self.__width

    @width.setter
    def width(self, value: int) -> None:

        """method to set the value of width"""

        if not isinstance(value: int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            return self.__width = value

    @property
    def height(self) -> int:
        """method to get the value of height"""

        return self.__height

    @height.setter
    def height(self, value: int) -> None:

        """method to set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        else:
            return self.__height = value
