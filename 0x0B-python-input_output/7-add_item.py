#!/usr/bin/python3
"""File name : 7-add_item.py"""

import sys
import os.path


load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

my_list = []
if os.path.("add_item.json"):
    my_list = load_file("add_item.json")
for arg in sys.argv[1:]:
    my_list.append(arg)

save_file(my_list, "add_item.json")
