# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def abbrev_name(name):    
    name = [i for i in name.lower().title() if i.isupper()]
    name.append('')
    name[2] = name[1]
    name[1] = '.'
    return "".join(name)