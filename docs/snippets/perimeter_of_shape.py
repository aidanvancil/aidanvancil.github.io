# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def perimeter_of_shape(*sides)->int:
  count = 0
  for i in sides:
     count += i
  return count