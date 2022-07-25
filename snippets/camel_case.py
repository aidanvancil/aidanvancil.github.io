# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def variable_to_camel_case(var: str) -> str:
    camel_case = ''
    camel_case += var[0].lower()
    for i in var[1:]:
        if i.isupper():
            camel_case += '_' + i.lower()
        else:
            camel_case += i
    return camel_case
            
        