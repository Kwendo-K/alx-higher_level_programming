#!/usr/bin/python3
"""a module that saves contents to a file in json format"""


def to_json_string(my_obj):
    """
    writing json data to a file
    args: my_obj
    return: jsos file
    """
    import json

    return json.dumps(my_obj)
