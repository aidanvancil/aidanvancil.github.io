# -*- coding: utf-8 -*-
"""

@author: aidan
"""
import numpy as np

def is_palindrome(prod: int) -> bool:
    temp = str(prod)
    if (temp[::-1] == temp):
        return True
    else:
        return False
            
    
def largest_palindrome_product() -> int:
    x2 = 999
    best = []
    while (x2 > 1):
        for i in reversed(range(1, 999)):
            if (is_palindrome(i * x2)):
                best.append(i * x2)
        x2 -= 1
    max_value = np.max(best)
    return max_value
    
    
        
        
            
        
            