#!/usr/bin/python3
"""
Docstring for python-more_classes.0-rectangle
"""


class Rectangle:
    """
    Docstring for Rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    def set_width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            self.__width = value
    def set_height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            self.__height = value
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
