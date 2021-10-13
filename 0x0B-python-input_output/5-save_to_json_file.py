#!/usr/bin/python3
"""
module: 5 saving json data to a file
"""


def save_to_json_file(my_obj, filename):
    """
    saving json data
    args:
    my_obj, filename
    """
    import json

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
