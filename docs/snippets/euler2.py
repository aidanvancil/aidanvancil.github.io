# -*- coding: utf-8 -*-
"""
@author: aidan
"""
    
def euler2(limit: int) -> int:
    buffer = [0, 1, 2]
    for i in range(2, limit+1):
        buffer.append(buffer[i]+buffer[i-1])
    return buffer