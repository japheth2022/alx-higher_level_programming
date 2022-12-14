#!/usr/bin/python3

"""define a class rectangle"""


class Rectangle:

    """represents class rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """initializes new rectangle"""
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):

        """sets and gets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):

        if type(vlue) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """sets and gets tha value of height"""
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
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    @property
    def perimeter(self):
        """ returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returns printable rep of the rectangle.
        represents thr rectangle with # character
        """
        if self.__width == 0 or self.__height == 0:
            return("")
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return("".join(rect))

    def __repr__(self):

        """returns string representation of rectangle"""

        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):

        """print a message for every deletion of rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
