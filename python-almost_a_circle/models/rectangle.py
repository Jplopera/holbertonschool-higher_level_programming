#!/usr/bin/python3
"""Module that contains "Rectangle" class"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle Inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """"Initialize Rectangle instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value"""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle"""
        for m in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for n in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """__str__ method that returns a string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates attributes"""
        if args is not None and len(args) is not 0:
            list_u = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_u[i], args[i])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method that returns a dictionary"""
        my_dict = {'id': self.id, 'width': self.width, 'height': self.height,
                   'x': self.x, 'y': self.y}
        return my_dict
