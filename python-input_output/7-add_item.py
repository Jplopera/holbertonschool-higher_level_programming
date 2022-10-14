#!/usr/bin/python3
"""Adds all arguments to a Python list and then save them to a file."""


from genericpath import isfile
import json
import sys
import os.path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

my_file = "add_item.json"
if os.path.isfile(my_file):
    obj = load_from_json_file(my_file)
else:
    obj = []
obj.extend(sys.argv[1:])
save_to_json_file(obj, my_file)
