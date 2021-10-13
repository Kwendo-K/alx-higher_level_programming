#!/usr/bin/python3
"""
module 6 loads object from json file
"""


def load_from_json_file(filename):
    """
    args: filename
    """
    import json

    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
