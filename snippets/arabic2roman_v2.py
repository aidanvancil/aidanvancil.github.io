# -*- coding: utf-8 -*-
"""
@author: aidan
"""



def arabic2roman_v2(a: int) -> str:
    roman_numerals = {1:'I',5:'V',10:'X',50:'L',100:'C'}
    sub_str = ""
    for n in sorted(roman_numerals.keys(), reverse = True):
        while a >= n:
            sub_str += roman_numerals[n]
            a -= n
    return sub_str            
        
         
        

print(arabic2roman_v2(25))