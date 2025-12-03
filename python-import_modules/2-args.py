#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    lenarg = len(argv)
    if lenarg == 0:
        print("0 arguments.")
    elif lenarg == 1:
        print("{} argument:".format(lenarg))
    else:
        print("{} arguments:".format(lenarg))
    for i in range(0, lenarg):
        print("{}: {}".format(i+1, argv[i]))
