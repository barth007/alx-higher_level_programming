#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg_number = len(sys.argv)
    only_arg = arg_number - 1
    if arg_number == 1:
        print("{} arguments.".format(only_arg))
    elif arg_number == 2:
        print("{} argument: " .format(only_arg))
        for i in range(1, arg_number):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments: ".format(only_arg))
        for i in range(1, arg_number):
            print("{}: {}".format(i, sys.argv[i]))
