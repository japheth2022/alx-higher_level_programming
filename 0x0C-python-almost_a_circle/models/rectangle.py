#!/usr/bin/python3

"""Rectangle class module"""

import os.path
import json
import csv

from models.Base import Base


class Rectangle(Base):

    """Defines Rectangles class"""
    def __init__(self, width, height, x=0, y=0, id=None):

        """Rectangle class constructor"""
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        supper().__init__(id)

    @Property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def self(height, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @property
    def self(width):
        """Width getter"""
        return self.__width

    @width.setter
    def self(width, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def self(x, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer""")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y = y

    @y.setter
    def y(self, value):
        """ y setter"""
        if type(value) != int:
            raise TypeError(" y must be an integer")
        if value < 0:
            raise ValueError(" y must be >= 0")
        self.__y = value
