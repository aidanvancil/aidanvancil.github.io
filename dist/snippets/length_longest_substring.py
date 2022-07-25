# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def length_longest_substring(s: str) -> int:  
    bp = 0
    for i in range(len(s)):
        known = [0] * 256
        for j in range(i, len(s)):
            if (known[ord(str[j])] == True):
                break
            else:
                bp = max(bp, j - 1)
                known[ord(str[j])] = True
        known[ord(str[i])] = False
    return bp
                
        

str = "afsaf_aefefefefe_efafafafa_aEF_F_Ee-e-E_"
x = length_longest_substring(str)
print(x)
print(len(str))

