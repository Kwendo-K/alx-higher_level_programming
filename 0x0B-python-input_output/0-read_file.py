#!/usr/bin/python3
"""this function reads contents from a file"""


def read_file(filename=""):
    with open(filename, mode='r', encoding='UTF8') as f:
        print(f.read(), end="")
