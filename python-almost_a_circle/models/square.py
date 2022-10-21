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

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes"""
        if args is not None and len(args) is not 0:
            list_u = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_u[i], args[i])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method that returns a dictionary"""
        my_dict = {'id': self.id, 'size': self.size,
                   'x': self.x, 'y': self.y}
        return my_dict
