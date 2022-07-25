# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def split_Even_Odd_Sublist(num_array): 
    odd = []
    even = []
    for i in num_array:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd