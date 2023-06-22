# -*- coding: utf-8 -*-
"""
@author: aidan
"""

roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}

def arabic2roman(a: int) -> str:
    sub_str = ""
    #roman_numerals.keys()
    while a > 0:
        if (a - 100) >= 0:
            sub_str+="C"
            a -= 100
        elif (a - 50) >= 0:
            sub_str+="L"
            a -= 50
        elif (a - 10) >= 0:
            sub_str+="X"
            a -= 10
        elif (a - 5) >= 0:
            sub_str+="V"
            a -= 5
        else:
            sub_str+="I"
            a -= 1
    return sub_str

print(arabic2roman(25))