#!/usr/bin/python3
def roman_to_int(roman_string):
    alphabet = {'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    result = 0
    if roman_string.isalpha() or roman_string == None:
        return 0
    else:
        for i in roman_string:
            result += alphabet[i]
