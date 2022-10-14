#!/usr/bin/python3
"""Creates a Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square inherited from rectangle"""

    def __init__(self, size):
        """initializes a Sqare"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of the instance"""
        return self.__size ** 2

    def __str__(self):
        """"""
        return str("[Square] {}/{}".format(self.__size, self.__size))
