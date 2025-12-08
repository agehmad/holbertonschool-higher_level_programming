#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0 #number of real elements
    for i in range(0, x):
        try:
            print(my_list[i], end='')
            n += 1
            continue
        except IndexError:
            break
    print(n)
