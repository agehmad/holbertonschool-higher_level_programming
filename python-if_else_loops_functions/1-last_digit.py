#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lnumber = abs(number)%10
if number > 0:
    if lnumber > 5:
        print("Last digit of", number, "is", lnumber, "and is greater than 5")
    elif lnumber < 6 and lnumber != 0:
        print("Last digit of", number, "is", lnumber, "and is less than 6 and not 0")
    else:
        print("Last digit of", number, "is", lnumber, "and is 0")
else:
    if lnumber == 0:
        print("Last digit of", number, "is", lnumber, "and is 0")
    else:
        lnumber = -lnumber
        print("Last digit of", number, "is", lnumber, "and is less than 6 and not 0")
