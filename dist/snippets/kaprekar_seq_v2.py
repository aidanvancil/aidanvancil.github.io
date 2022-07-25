# -*- coding: utf-8 -*-
"""
@author: aidan
"""

#Take any four-digit number, using at least two different digits (leading zeros are allowed). Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary. Subtract the smaller number from the bigger number. Go back to step 2 and repeat. This process stops after a few steps, that is step 3 produces the same number. DO this with paper and pen to understand the same Start with  1945 
#
#9541–1459=8082 
#
#8820–0288=8532 
#
#8532–2358=6174 
#
#7641–1467=6174 
#
#Given a suitable starting number generate the sequence, stopping the output without any repetition.
#For example if 1945 is input it should return  [1945,8082,8532,6174] 



def kaprekar_seq(n:int, LIMIT: int)->[int]:
    kaprekar = [n]
    for i in range(0, LIMIT):
        formatted = ascending(n, True)
        formatted_temp = ascending(n, False)
        n = formatted - formatted_temp
        kaprekar.append(n)
    return kaprekar

def ascending(n: int, condition: bool):
    if True:
        return int("".join(sorted(str(n), reverse=True)))
    else:
        return int("".join(sorted(str(n))))
    