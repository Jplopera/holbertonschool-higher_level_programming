#!/usr/bin/python3
"""Define an empty class square"""


class Square:
    """empty class Square"""

    def __init__(self, size=0):
        """Instantiation with size"""
        self.__size = size

    def area(self):
        """instance method that returns the current square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """etrieves the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
