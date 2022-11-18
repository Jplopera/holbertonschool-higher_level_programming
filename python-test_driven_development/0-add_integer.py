#!/usr/bin/python3
"""Module that contains the funtions to add two numbers"""


def add_integer(a, b=98):
    """Function that returns the sum of two numbers"""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
