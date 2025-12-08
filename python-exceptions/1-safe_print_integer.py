#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if int(value) == value
        print("{}".format(value))
    except TypeError:
        print("{} is not an integer".format(value))
