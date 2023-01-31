#!/usr/bin/python3
"""File name : 7-add_item.py"""

import sys  # import sys module
import os.path  # import os.path module


load_file = __import__('6-load_from_json_file').load_from_json_file # import load_from_json_file function from 6-load_from_json_file.py
save_file = __import__('5-save_to_json_file').save_to_json_file # import save_to_json_file function from 5-save_to_json_file.py

my_list = [] # create empty list
if os.path.exists("add_item.json"): # if file exists
    my_list = load_file("add_item.json") # load file into my_list

for arg in sys.argv[1:]: # iterate through arguments
    my_list.append(arg) # append argument to my_list

save_file(my_list, "add_item.json") # save my_list to file
