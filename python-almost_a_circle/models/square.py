#!/usr/bin/python3
"""Module that contains "Square" class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square Inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """"Initialize Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ method that returns a string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
