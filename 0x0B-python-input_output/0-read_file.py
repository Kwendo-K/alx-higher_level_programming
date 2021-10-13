#!/usr/bin/python3
"""
this functions reads contents from a file
args: filename, mode, encoding
"""


def read_file(filename=""):
    with open(filename, mode='r', encoding='UTF8') as f:
        print(f.read(), end="")
