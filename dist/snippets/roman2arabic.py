# -*- coding: utf-8 -*-
"""
@author: aidan
"""

roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}

def roman2arabic(r:str) -> int:
    count = 0
    for i in r:
        if i in roman_numerals:
            count += roman_numerals[i]
    return count

count = roman2arabic("XIVLII")
print(count)