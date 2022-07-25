# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def vowel_to_upper_cons_to_lower(string: str)-> str:
    string_lower = string.lower()
    vowels = 'aieou'
    for letter in string_lower:
        if letter in vowels:
            string_new = string_lower.replace(letter, letter.upper())
    return string_new