# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def count_vowel_and_cons(filename: str)-> (int, int):
    with open(filename) as file:
        lines = file.read()
        file.close()
    vowel_c, cons_c = 0, 0
    vowels = {'a','e','i','o','u'}
    for line in lines.strip():
        if line.lower() in vowels:
            vowel_c += 1
        else:
            if line.isalpha():
                cons_c += 1
    return vowel_c, cons_c

count_vowel_and_cons("content.txt")