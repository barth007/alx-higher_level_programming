#!/usr/bin/python3
# 1-write_file.py

def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as  myFile:
        read_file = myFile.write(text)
    return (read_file)
