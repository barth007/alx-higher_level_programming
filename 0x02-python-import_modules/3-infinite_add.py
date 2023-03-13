#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv)
    if num_args == 1:
        print("{:d}".format(0))
    else:
        add = 0
        for i in range(1, num_args):
            num = int(sys.argv[i])
            add = add + num
        print("{:d}".format(add))
