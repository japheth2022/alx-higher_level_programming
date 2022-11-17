#!/usr/bin/python3
"""Defines a method to save an object in json representation"""

import json


def save_to_json_file(my_obj, filename):
    """write object to a file using json representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, filename)
