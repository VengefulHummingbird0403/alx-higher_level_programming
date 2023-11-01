#!/usr/bin/python3
"""Defines a class rectangle and calculates area and perimeter"""


class Rectangle:
    """
    A class used to represent a rectangle

    Properties
    ----------
    width : int
        integer representing the width of the rectangle
    height : int
        the height of the rectangle

    Methods
    -------
    area()
        returns the area of the rectangle
    perimiter()
        returns the perimeter
    """

    def __init__(self, width=0, height=0):
        """
        when arguments are not passed, default are used

        Parameters
        ----------
        width : int, optional
            The width of the rectangle (default is 0)
        height : int, optional
            The height of the rectange (default is 0)
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle's width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieve the rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle's height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the rectangle's area"""
        return self.width * self.height

    def perimeter(self):
        """Returns rectangle perimeter"""
        # if either measurement is 0, return 0
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2
