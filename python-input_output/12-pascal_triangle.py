#!/usr/bin/python3
"""
Docstring for python-input_output.12-pascal_triangle
"""


def pascal_triangle(n):
    """
    Docstring for pascal_triangle

    :param n: Description
    """
    if n <= 0:
        return []
    else:
        triangle = [[1], [1,1]]
        for i in range(2, n):
            newlist = []
            newlist.append(1)
            for j in range(0, i-1):
                newlist.append(triangle[i-1][j] + triangle[i-1][j+1])
            newlist.append(1)
            triangle.append(newlist)
        for a in triangle:
            print(a)
