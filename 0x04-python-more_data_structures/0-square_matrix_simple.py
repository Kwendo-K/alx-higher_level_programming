#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    sqr = []
    for i in matrix:
        sqr.append(list(map(lambda x: x * x, i)))
    return sqr
