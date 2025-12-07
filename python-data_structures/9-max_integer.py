#!/usr/bin/python3
def max_integer(my_list=[]):
    a = my_list[0]
    for i in range(1, len(my_list)):
        if i > a:
            a = i
    return a
