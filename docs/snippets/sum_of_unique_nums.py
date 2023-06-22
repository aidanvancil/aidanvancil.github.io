# -*- coding: utf-8 -*-
"""
@author: aidan
"""


def sum_of_unique_numbers(num_list: [int])-> int:
    uniques = [i for i in num_list if num_list.count(i) == 1]
    return sum(uniques)
    