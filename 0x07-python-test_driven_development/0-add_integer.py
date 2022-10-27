#!/usr/bin/python3

"""module containing adder function for testing"""


def add_integer(a, b=98):

    """ adding integers"""
    if type(a) not in [float, int]:
        raise TypeError("a must be integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be integer")
    return int(a) + int(b)
