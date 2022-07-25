# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def special_pythag_triplet():
    SUM_PY = 1000
    for c in range(1000, 0, -1):
        for b in range(c, 0, -1):
            for a in range(b, 0, -1):
                if SUM_PY == (a + b + c) and (a**2 + b**2) == c**2:
                    return a*b*c
                    
                