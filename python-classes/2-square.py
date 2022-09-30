#!/usr/bin/python3
"""Define an empty class square"""


class Square:
    """empty class Square"""

    def __init__(self, size):
        """Instantiation with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
