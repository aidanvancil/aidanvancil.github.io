# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def mult_3_or_5(LIMIT: int) -> int:
    counter, total = 0, 0 #sum of multiples
    while (counter < LIMIT):
        if (counter % 3 == 0 or counter % 5 == 0):
            total += counter
        counter += 1
    return total
        