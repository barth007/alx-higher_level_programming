#!/usr/bin/python3
# 1-my_list.py

class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
