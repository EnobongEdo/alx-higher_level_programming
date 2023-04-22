#!/usr/bin/python3
"""
contains the javascript object notation(json) str function
"""

import json


def from_json_string(my_str):
    """returns an object represented by a JSON STRING"""
    return json.loads(my_str)
