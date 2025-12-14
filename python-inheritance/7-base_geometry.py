#!/usr/bin/python3
"""
Docstring for python-inheritance.7-base_geometry
"""


class BaseGeometry:
    """
    Docstring for BaseGeometry
    """
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
        else:
            self.value = value
