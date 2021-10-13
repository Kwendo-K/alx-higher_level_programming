#!/usr/bin/python3
import json
"""a module that saves contents to a file in json format"""


def to_json_string(my_obj):
    """writing json data to a file"""
    return json.dumps(my_obj)
