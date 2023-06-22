# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def prime_sequence(LIMIT: int)-> [int]:
    buffer = []
    for i in range (1, LIMIT+1):
        buffer.append(i)
    return list(filter(is_prime, buffer))

def is_prime(k: int):
    for i in range(2, int(k**.5)+1):
        if k % i == 0:
            return False
    return True
