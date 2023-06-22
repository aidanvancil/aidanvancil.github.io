# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def sum_of_two(nums: [int], target: int) -> [int]:
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i