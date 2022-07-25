# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def collatz_sequence(k: int) -> [int]:
    collatz = []
    while (k != 1):
           if k % 2 == 0:
               k /= 2
           else:
               k = k*3 + 1
           collatz.append(int(k))
    return collatz

#def collatz_sequence_updated(k: int) -> int:
#    if n in [1, 2, 4]:
 #       return 4
 #   while n != 4:
  #      if is_power_of_2(n):
   #         return n
    #    n = next_collatz(n)
