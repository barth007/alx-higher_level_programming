#!/usr/bin/python3
# 5-save_to_json_file.py
import json

def save_to_json_file(my_obj, filename):
    with open(filename, mode="w", ) as myFile:
        json_file = json.dump(my_obj, myFile)
    return (json_file)
