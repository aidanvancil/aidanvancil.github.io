# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def kaprekar_seq(n: int) -> [int]:
    kaprekar = []
    kaprekar.append(n)
    for i in range(0,3):
        ascending = sorted(str(n))[::-1]
        formatted_ascending = int("".join(ascending))
        n = formatted_ascending
        sort_int = sorted(str(n))
        res = int("".join(sort_int))
        temp = n - res
        kaprekar.append(temp)
        n = temp
    return kaprekar