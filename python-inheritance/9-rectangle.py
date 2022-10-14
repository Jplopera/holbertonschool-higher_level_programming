#!/usr/bin/python3
"""Creates a Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inhered of BaseGeometry"""

    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the instance"""
        return self.__width * self.__height

    def __str__(self):
        """return the square description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
