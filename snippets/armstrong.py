# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def armstrong(start: int, end: int) -> int:
    armstrong_nums = []
    temp_sum = 0
    for i in range(start, end + 1):
        temp_sum = 0
        exp = len(str(i))
        for j in str(i):
            temp_sum += int(j) ** exp
        if temp_sum == int(i):
            armstrong_nums.append(int(i))
    return sum(armstrong_nums)
            
armstrong(100, 500)