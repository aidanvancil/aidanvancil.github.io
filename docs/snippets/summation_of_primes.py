# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def summation_of_primes(N: int):
    # N = primes number limit
    primes = []
    primes.extend([i for i in range(N+1) if is_prime(i) and i > 1])
    return sum(primes)

def is_prime(k: int):
    for i in range(2, int(k**.5)+1):
        if k % i == 0:
            return False
    return True