#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:14:22 2020

@author: nicholas
"""

def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    for i in range(max(a, b), 0, -1):
        if a%i == 0 and b%i == 0:
            return i

a = 84
b = 72
print(gcd(a,b))