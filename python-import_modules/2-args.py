#!/usr/bin/python
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    lenarg = len(argv)
    if lenarg == 0:
        print("0 arguments.")
    elif lenarg > 0:
        print("{} arguments:".format(lenarg))
    for i in range(1, lenarg + 1):
        print("{}: {}".format(i, argv[i]))
