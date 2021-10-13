#!/usr/bin/python3
"""Module two appends contents into a file"""


def append_write(filename="", text=""):
    """appending files in utf-mode"""

    with open(filename, mode='a', encoding='utf-8') as f:
        return(f.write(text))
