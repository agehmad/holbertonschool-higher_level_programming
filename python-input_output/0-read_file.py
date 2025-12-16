#!/usr/bin/python3
def read_file(filename=""):
    """
    Docstring for read_file
    
    :param filename: Description
    """
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read())
