# -*- coding: utf-8 -*-
"""
@author: aidan
"""
def parse_even_nums(fib_nums: list)-> int:
    total = 0
    for i in range(0, len(fib_nums)):
        if ((fib_nums[i] % 2) == 0):
            total += int(fib_nums[i])
    return total

def Fib_numbers()-> int:
    fib_nums = [0,1]
    fib_value = 3999999 # 4 million minus starting 0 (so 4 mil minus 1)
    LIMIT = 5000        # max const limit
    for i in range(2, LIMIT):    
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
        if (fib_nums[i] > fib_value):
            del fib_nums[-1]
            break
    total = parse_even_nums(fib_nums)
    return total
        
    