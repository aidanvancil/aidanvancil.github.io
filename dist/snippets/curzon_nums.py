# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def is_curzon(num: int) -> bool:
    curz_condition = (2 ** num) + 1
    if ((curz_condition % (num * 2 + 1)) == 0):
        return True
    else:
        return False