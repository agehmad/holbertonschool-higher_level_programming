#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0] if len >= 1 else 0
    a2 = tuple_a[1] if len >= 2 else 0
    b1 = tuple_b[0] if len >= 1 else 0
    b2 = tuple_b[1] if len >= 2 else 0
    a = a1 + b1
    b = a2 + b2
    new_tuple = (a, b)
    return new_tuple
