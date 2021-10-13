#!/usr/bin/python3
"""
this functions reads contents from a file
args: filename
"""


def read_file(filename=""):
    with open(filename, 'r') as f:
        data = f.read()
        print(data)
