# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def repeat_sequence(string: str) -> str:
    counter = 0
    buffer = ""
    for i in string:
        if counter != 0:
            buffer += '->'
        if i not in buffer:
            buffer += i.title()
            buffer += i.lower() * counter
        counter += 1
    return buffer