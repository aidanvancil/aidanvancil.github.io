# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def solution(inputString):
    return ("".join([chr(ord(i) + 1) for i in inputString])).replace('{', 'a')