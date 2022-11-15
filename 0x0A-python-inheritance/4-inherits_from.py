#!/usr/bin/python3

"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):

    """Checks if an object is na inherited instance of a class

    Args:
        obj(any): The object to be checked
        a_class(type): The class where the object is searched

    Returns:
    True - If object is an inherited instance of a class
    False - Otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
