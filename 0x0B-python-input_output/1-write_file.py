#!/usr/bin/python3
"""module-1 wrtites content into a file"""


def write_file(filename="", text=""):
    """writing contents into a file in utf-8 format"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return(f.write(text))
