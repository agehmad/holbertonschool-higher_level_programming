#!/usr/bin/python3
"""
Docstring for python-input_output.7-add_item
"""
import json
import sys

def load_from_json_file(filename):
    """
    Docstring for load_from_json_file

    :param filename: Description
    """
    with open(filename, encoding='utf-8') as a_file:
        data = json.load(a_file)
    return data

def save_to_json_file(my_obj, filename):
    """
    Docstring for save_to_json_file

    :param my_obj: Description
    :param filename: Description
    """

    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(json.dumps(my_obj))

save_to_json_file(sys.argv, add_item.json)
