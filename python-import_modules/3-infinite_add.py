#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    result = 0
    for i in range(0, len(argv)+1):
        result += int(argv[i])
    print(result)

