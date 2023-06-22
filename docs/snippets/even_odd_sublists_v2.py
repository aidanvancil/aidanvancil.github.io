# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def split_even_odd_sublist(num_list: [int]) -> ([int], [int]):
    new_odd  = list(map(odd, num_list))
    new_even = list(map(even, num_list))
    return ([i for i in new_even if i != None], [i for i in new_odd if i != None])

def odd(i: int):
    if i%2 != 0:
        return i
    pass

def even(i: int):
    if i%2 == 0:
        return i
    pass
        
    #even =[(j in num_list) for j in odd_even if j == 0]
    #odd = [(j in num_list) for j in odd_even if j == 1]