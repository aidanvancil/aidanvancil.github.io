# -*- coding: utf-8 -*-
"""
@author: aidan
"""
    
def up_to_n(n: int):
    LIMIT = 10
    counter = 1
    condition = True
    for i in range(0, LIMIT):
        if not condition:
            break
        for j in range(0, i):
            print(counter, end=" ")
            counter += 1
            if counter == n:
                condition = False
                break
        print("\r")
    print("**")
 
up_to_n(290)