#!/usr/bin/python3
# 6-load_from_json_file.py
import json

def load_from_json_file(filename):
    with open(filename, mode="r") as myFile:
        loaded_file = json.load(myFile)
    return (loaded_file)
