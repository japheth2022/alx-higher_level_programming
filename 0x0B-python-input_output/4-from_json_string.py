#!/usr/bin/python3

"""converts json to python data structure"""

import json


def from_json_string(my_str):
    """converts Json to string object"""
    return json.loads(my_str)
