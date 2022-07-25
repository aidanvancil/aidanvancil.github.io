# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def max_factor(num):
    """Find the maximum prime factor."""
    best = None
    factor = 2 
    while factor * factor <= num:
        while num % factor == 0:
            best = factor
            num /= factor
        factor += 1
    if (num > 1): 
        return num 
    return best

