#!/usr/bin/python3
"""module for reads json file and copies to a string"""


def from_json_string(my_str):
    """
    reading json files
    args:
    my_str
    return an object
    """
    import json

    return json.loads(my_str)
