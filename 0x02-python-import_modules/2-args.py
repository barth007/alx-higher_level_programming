#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg_number = len(sys.argv) - 1
    if arg_number == 0:
        print("{} arguments.".format(arg_number))
    else:
        print("{} argument{}".format(arg_number,
              's'if arg_number != 1 else ' '))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
