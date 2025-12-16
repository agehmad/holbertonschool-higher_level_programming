#!/usr/bin/python3
"""Module for reading and printing UTF-8 text files"""


def read_file(filename=""):
    """
    Docstring for read_file
    
    :param filename: Description
    """
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read())
