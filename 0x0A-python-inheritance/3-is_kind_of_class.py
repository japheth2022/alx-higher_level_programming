#!/usr/bin/python3

"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):

    """Check whether an object is an instance or inherited instance of a class

    Args:
        obj(any): Object to check
        a_class(type): The class where the object is checked

        Returns:
            True-if the object is an instance or is inherited instance of
            the a_class
            False - Otherwise
    """

    if isinstance(obj, a_class):
        return True
    return False
