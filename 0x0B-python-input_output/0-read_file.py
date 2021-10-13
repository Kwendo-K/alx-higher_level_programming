#!/usr/bin/python3
"""a function that reads and outputs file contents"""


def read_file(filename=""):
    with open(filename, 'r') as f:
        data = f.read()
        print(data)
