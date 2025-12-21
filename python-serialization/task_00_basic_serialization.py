#!/usr/bin/python3
"""
Docstring for python-serialization.task_00_basic_serialization
"""


import json
def serialize_and_save_to_file(data, filename):
    with open(filename, 'w') as afile:
        json.dump(data, filename)

def load_and_deserialize(filename):
    with open(filename, 'r') as afile:
        return json.load(afile)
