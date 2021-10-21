#!/usr/bin/python3
"""
module 1: creating a base class
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __nb_objects =+ 1
            id = __nb_objects
