#!/usr/bin/python3
"""Define an empty class square"""


class Square:
    """empty class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with size"""
        self.__size = size
        self.__position

    def area(self):
        """instance method that returns the current square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieves the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter of position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print()
        for xj in range(self.__size):
            print("{}{}".format(" " * self.position[0], "#" * self.__size))
