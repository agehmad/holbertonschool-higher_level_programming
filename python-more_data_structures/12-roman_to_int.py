#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    alphabet = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0
    n = len(roman_string)
    for i in range(n):
        current_value = alphabet[roman_string[i]]
        if i < n - 1:
            next_value = alphabet[roman_string[i + 1]]
        else:
            next_value = 0
        if current_value < next_value:
            result -= current_value
        else:
            result += current_value
    return result
