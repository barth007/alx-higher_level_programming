#!/usr/bin/python3

# 7-add_item.py
import sys
import json
from os.path import isfile
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = 'add_item.json'
is_File= isfile(file_name)
arg_list = []
if not is_File:
    load_from_json_file(file_name)
arg_list += sys.argv[1:]
#arg_list.extend(sys.argv[1:])
save_to_json_file(arg_list, file_name)
