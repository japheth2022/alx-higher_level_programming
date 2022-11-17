#!/usr/bin/python3

"""converts an object to json file"""

import json


def to_json_string(my_obj):
    """Returns json representation of an object """
    return json.dumps(my_obj)
