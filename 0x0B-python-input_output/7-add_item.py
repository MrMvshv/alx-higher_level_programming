#!/usr/bin/python3
""" adds all arguments to a
    python list, saves them
    to a file
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

args = sys.argv[1:]

try:
    list1 = load_from_json_file("add_item.json")
except NameError:
    list1 = []

list1.extend(args)
save_to_json_file(list1, "add_item.json")
