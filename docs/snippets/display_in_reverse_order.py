# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def display_in_reverse_order(*strings):
    sub_str = []
    for i in strings:
        sub_str += "".join(i)
    return  str("".join(sub_str[::-1]))