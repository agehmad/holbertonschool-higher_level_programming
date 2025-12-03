#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    result = 0
    for i in range(0, len(argv)):
        result += int(i)
    print(result)

