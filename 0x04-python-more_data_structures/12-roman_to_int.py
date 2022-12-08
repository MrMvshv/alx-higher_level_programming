#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    elif type(roman_string) is not str:
        return 0
    else:
        dict = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000
        }
        total = 0
        prev = 1001
        for x in roman_string:
            print(x)
            print(prev)
            print(dict[x])
            if dict[x] > prev:
                total += dict[x] - prev 
            else:
                total += dict[x]
            prev = dict[x]
        return total
