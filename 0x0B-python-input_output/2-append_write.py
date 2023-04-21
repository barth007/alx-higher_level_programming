#!/usr/bin/python3
# 2-append_write.py
def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as myFile:
        append_file = myFile.write(text)
    return (append_file)
