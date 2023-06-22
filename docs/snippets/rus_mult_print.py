# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def rus_mult_print(a: int, b: int) -> None:
    PLUS = ' +'
    CROSS = ' x'
    buffer = ""
    answer = 1
    for i in range(0, 4):
        buffer += str(a) + ' ' + str(b)
        a //= 2
        b *= 2
        if i % 2 == 0:
            buffer += PLUS + '\n'
            answer += a + b
        else:
            buffer += CROSS + '\n'
    buffer += '= ' + str(answer)
    print(buffer)