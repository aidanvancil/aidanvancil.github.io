# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def up_to_n_v2(n: int, LIMIT: int):
    holding = ''
    counter = 1
    for i in range(0, LIMIT):
        for j in range(0, i):
            holding = listing(holding, counter)
            counter += 1    # rip counter++ :((((
            if counter == n:
                break
        holding += "\r"
    holding += "**"
    return holding
    

def listing(holding: str, counter: int):
    holding += str(counter) + '\0'
    return holding
 
up_to_n_v2(290, 10)