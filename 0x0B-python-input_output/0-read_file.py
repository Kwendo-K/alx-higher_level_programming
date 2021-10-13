#!/usr/bin/python3
"""this function reads contents from a file"""


def read_file(filename=""):
    """reading file contents in utf-8 format"""
    with open(filename, encoding='utf-8') as f:
        data = f.read()
        print(data, end="")
