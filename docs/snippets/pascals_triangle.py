# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def pascal_output(size: int) -> str:
    for i in range(size):
        print(' '*(size-i), end='')
        print(' '.join(map(str,str (11**i))))
    
pascal_output(15)