#!/usr/bin/python3

"""Base class module"""

import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        self.__nb_objects = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
