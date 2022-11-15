#!/usr/bin/python3

"""Defines a function that checks a class"""


def is_same_class(obj, a_class):
    """Check if an object is an instance of  class
    Args:
        obj(any): The object to be checked
        a_class(type): The class where the object is checked

    Returns:
        True - if the object is an exactly an instance of a given class
        False - otherwise
    """

    if type(obj) == a_class:
        return(True)
    return(False)
