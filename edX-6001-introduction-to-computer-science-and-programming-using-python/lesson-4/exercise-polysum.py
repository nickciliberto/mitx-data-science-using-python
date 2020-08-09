# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:48:31 2020

@author: nciliber
"""

import math

def polysum(n,s):
    area = (0.25*n*s**2)/math.tan(math.pi/n)
    perimeter = n*s
    return round(area+perimeter**2,4)