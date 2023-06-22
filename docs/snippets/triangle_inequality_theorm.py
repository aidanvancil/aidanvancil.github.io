# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def is_valid_triangle(side1: int, side2:int, side3:int) -> bool:
  if ((side1 + side2) > side3 and (side2 + side3) > side1 and (side1 + side3) > side2):
      return True
  else:
      return False

